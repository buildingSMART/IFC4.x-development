"""GitHub pull-request workflow for the IFC structural merge driver."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

try:
    from . import xmi_merge
except ImportError:  # Executed directly instead of as a package.
    import xmi_merge  # type: ignore[no-redef]

STATE_VERSION = 3
STATE_NAME = "ifc-pr-merge-state.json"
PR_JSON_FIELDS = (
    "number,title,headRefName,headRefOid,headRepositoryOwner,"
    "baseRefName,baseRefOid,isDraft,url,author,updatedAt,state,mergedAt,mergeCommit"
)
SELECTABLE_PR_STATES = {"OPEN", "MERGED", "CLOSED"}
LIST_PR_STATES = {"all", "open", "merged", "closed"}
BRACKETED_CODE_RE = re.compile(r"\[([A-Za-z]+[0-9]+)\]")
LOOSE_CODE_RE = re.compile(r"(?<![A-Za-z0-9])([A-Za-z]+[0-9]+)(?![A-Za-z0-9])")


class WorkflowError(RuntimeError):
    """Raised for an actionable PR workflow error."""


@dataclass(frozen=True)
class PullRequest:
    number: int
    title: str
    head_ref: str
    head_oid: str
    head_owner: str
    base_ref: str
    base_oid: str
    is_draft: bool
    state: str
    url: str
    author: str
    updated_at: str
    merged_at: str | None
    merge_oid: str = ""

    @classmethod
    def from_gh(cls, value: dict[str, Any]) -> PullRequest:
        head_owner = value.get("headRepositoryOwner") or {}
        author = value.get("author") or {}
        merged_at = value.get("mergedAt")
        return cls(
            number=int(value["number"]),
            title=str(value["title"]),
            head_ref=str(value.get("headRefName") or ""),
            head_oid=str(value.get("headRefOid") or ""),
            head_owner=str(head_owner.get("login") or head_owner.get("name") or ""),
            base_ref=str(value.get("baseRefName") or ""),
            base_oid=str(value.get("baseRefOid") or ""),
            is_draft=bool(value["isDraft"]),
            state=str(value.get("state") or "OPEN").upper(),
            url=str(value["url"]),
            author=str(author.get("login") or author.get("name") or ""),
            updated_at=str(value["updatedAt"]),
            merged_at=str(merged_at) if merged_at is not None else None,
            merge_oid=str((value.get("mergeCommit") or {}).get("oid") or ""),
        )


@dataclass
class MergeState:
    version: int
    remote: str
    repository: str
    branch: str
    start_head: str
    pr_ref: str
    fetched_oid: str
    replay_oid: str
    commit_message: str
    started_at: str
    pull_request: dict[str, Any]
    base: str | None = None
    include_drafts: bool = False
    remaining_selectors: list[str] | None = None
    labels: list[str] | None = None


def _run(
    args: Sequence[str],
    repo_root: Path,
    *,
    check: bool = True,
    capture: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    process = subprocess.run(
        list(args),
        cwd=repo_root,
        env=env,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        check=False,
    )
    if check and process.returncode:
        message = (process.stderr or process.stdout or "").strip()
        raise WorkflowError(message or f"command failed: {shlex.join(args)}")
    return process


def _git(
    repo_root: Path,
    *args: str,
    check: bool = True,
    capture: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    return _run(
        ["git", *args],
        repo_root,
        check=check,
        capture=capture,
        env=env,
    )


def _config(repo_root: Path, key: str) -> str | None:
    process = _git(repo_root, "config", "--get", key, check=False)
    if process.returncode:
        return None
    return process.stdout.strip() or None


def _remote_name(repo_root: Path, requested: str | None) -> str:
    remote = requested or _config(repo_root, "ifc.remote") or "origin"
    process = _git(repo_root, "remote", "get-url", remote, check=False)
    if process.returncode:
        raise WorkflowError(f"Git remote {remote!r} does not exist")
    return remote


def _repository_name(repo_root: Path, remote: str) -> str:
    remote_url = _git(repo_root, "remote", "get-url", remote).stdout.strip()
    process = _run(
        ["gh", "repo", "view", remote_url, "--json", "nameWithOwner"],
        repo_root,
        check=False,
    )
    if process.returncode:
        message = (process.stderr or process.stdout).strip()
        raise WorkflowError(
            f"cannot resolve GitHub repository for remote {remote!r}: {message}"
        )
    return str(json.loads(process.stdout)["nameWithOwner"])


def list_pull_requests(
    repo_root: Path,
    repository: str,
    *,
    base: str | None = None,
    labels: Sequence[str] | None = None,
    limit: int = 100,
    state: str = "all",
) -> list[PullRequest]:
    if state not in LIST_PR_STATES:
        raise WorkflowError(f"unsupported PR state filter {state!r}")
    gh_states = ("all",) if state == "all" else (state,)
    pull_requests: list[PullRequest] = []
    for gh_state in gh_states:
        command = [
            "gh",
            "pr",
            "list",
            "--repo",
            repository,
            "--state",
            gh_state,
            "--limit",
            str(limit),
            "--json",
            PR_JSON_FIELDS,
        ]
        if base:
            command.extend(["--base", base])
        if labels:
            for label in labels:
                command.extend(["--label", label])
        process = _run(command, repo_root)
        pull_requests.extend(
            pr
            for pr in (PullRequest.from_gh(value) for value in json.loads(process.stdout))
            if pr.state in SELECTABLE_PR_STATES
        )
    pull_requests.sort(key=lambda pr: pr.updated_at, reverse=True)
    return pull_requests[:limit]


def get_pull_request(
    repo_root: Path, repository: str, number: int
) -> PullRequest:
    process = _run(
        [
            "gh",
            "pr",
            "view",
            str(number),
            "--repo",
            repository,
            "--json",
            PR_JSON_FIELDS,
        ],
        repo_root,
    )
    value = json.loads(process.stdout)
    pr = PullRequest.from_gh(value)
    if pr.state not in SELECTABLE_PR_STATES:
        raise WorkflowError(
            f"pull request #{number} is {pr.state.lower()}; only open, merged, or closed "
            "pull requests can be processed"
        )
    return pr


def _normalise_selector(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def pull_request_code(pr: PullRequest) -> str | None:
    for value in (pr.title, pr.head_ref.rsplit("/", 1)[-1], pr.head_ref):
        bracketed = BRACKETED_CODE_RE.search(value)
        if bracketed:
            return bracketed.group(1).upper()
    for value in (pr.title, pr.head_ref.rsplit("/", 1)[-1], pr.head_ref):
        loose = LOOSE_CODE_RE.search(value)
        if loose:
            return loose.group(1).upper()
    return None


def _natural_key(value: str) -> tuple[tuple[int, str | int], ...]:
    parts: list[tuple[int, str | int]] = []
    for part in re.split(r"([0-9]+)", value.casefold()):
        if not part:
            continue
        if part.isdigit():
            parts.append((1, int(part)))
        else:
            parts.append((0, part))
    return tuple(parts)


def pull_request_order_key(pr: PullRequest) -> tuple[object, ...]:
    code = pull_request_code(pr)
    if code:
        return (0, _natural_key(code), pr.number)
    return (1, _natural_key(pr.title), pr.number)


def sort_pull_requests_by_code(pull_requests: Sequence[PullRequest]) -> list[PullRequest]:
    return sorted(pull_requests, key=pull_request_order_key)


def selectable_pull_requests_by_code(
    repo_root: Path,
    repository: str,
    *,
    base: str | None = None,
    labels: Sequence[str] | None = None,
    limit: int = 1000,
    include_drafts: bool = False,
) -> list[PullRequest]:
    pull_requests = list_pull_requests(
        repo_root, repository, base=base, labels=labels, limit=limit, state="all"
    )
    if not include_drafts:
        pull_requests = [pr for pr in pull_requests if not pr.is_draft]
    return sort_pull_requests_by_code(pull_requests)


def select_pull_request(
    pull_requests: Sequence[PullRequest], selector: str
) -> PullRequest:
    selector = selector.strip()
    number_match = re.fullmatch(r"#?(\d+)", selector)
    if number_match:
        number = int(number_match.group(1))
        matches = [pr for pr in pull_requests if pr.number == number]
        if not matches:
            raise WorkflowError(f"no open or merged pull request #{number}")
        return matches[0]

    folded = selector.casefold()
    normalised = _normalise_selector(selector)
    exact = [
        pr
        for pr in pull_requests
        if folded
        in {
            pr.head_ref.casefold(),
            pr.head_ref.rsplit("/", 1)[-1].casefold(),
            pr.title.casefold(),
        }
        or normalised
        in {
            _normalise_selector(pr.head_ref),
            _normalise_selector(pr.head_ref.rsplit("/", 1)[-1]),
            _normalise_selector(pr.title),
        }
    ]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise WorkflowError(
            f"selector {selector!r} matches multiple pull requests: "
            + ", ".join(f"#{pr.number} {pr.head_ref}" for pr in exact)
        )

    partial = [
        pr
        for pr in pull_requests
        if folded in pr.head_ref.casefold()
        or folded in pr.title.casefold()
        or (normalised and normalised in _normalise_selector(pr.title))
    ]
    if len(partial) == 1:
        return partial[0]
    if not partial:
        raise WorkflowError(f"no open or merged pull request matches {selector!r}")
    raise WorkflowError(
        f"selector {selector!r} is ambiguous: "
        + ", ".join(f"#{pr.number} {pr.head_ref}" for pr in partial)
    )


def _print_pull_requests(pull_requests: Sequence[PullRequest]) -> None:
    if not pull_requests:
        print("No open or merged pull requests.")
        return
    number_width = max(3, max(len(str(pr.number)) for pr in pull_requests))
    state_width = max(5, max(len(pr.state) for pr in pull_requests))
    base_width = max(4, max(len(pr.base_ref) for pr in pull_requests))
    head_width = max(4, max(len(pr.head_ref) for pr in pull_requests))
    print(
        f"{'PR':>{number_width + 1}}  "
        f"{'STATE':<{state_width}}  "
        f"{'BASE':<{base_width}}  "
        f"{'HEAD':<{head_width}}  "
        "TITLE"
    )
    for pr in pull_requests:
        draft = " [draft]" if pr.is_draft else ""
        number = f"#{pr.number}"
        print(
            f"{number:>{number_width + 1}}  "
            f"{pr.state:<{state_width}}  "
            f"{pr.base_ref:<{base_width}}  "
            f"{pr.head_ref:<{head_width}}  "
            f"{pr.title}{draft}"
        )


def _state_path(repo_root: Path) -> Path:
    output = _git(
        repo_root,
        "rev-parse",
        "--path-format=absolute",
        "--git-path",
        STATE_NAME,
    ).stdout.strip()
    return Path(output)


def _load_state(repo_root: Path) -> MergeState | None:
    path = _state_path(repo_root)
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        state = MergeState(**value)
    except (OSError, TypeError, ValueError) as exc:
        raise WorkflowError(f"cannot read merge state {path}: {exc}") from exc
    if state.version != STATE_VERSION:
        raise WorkflowError(
            f"unsupported merge-state version {state.version} in {path}"
        )
    return state


def _write_state(repo_root: Path, state: MergeState) -> None:
    path = _state_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(asdict(state), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _clear_state(repo_root: Path) -> None:
    _state_path(repo_root).unlink(missing_ok=True)


def _summary_entry(pr: PullRequest, status: str, reason: str = "") -> dict[str, Any]:
    return {
        "status": status,
        "number": pr.number,
        "code": pull_request_code(pr),
        "title": pr.title,
        "head_ref": pr.head_ref,
        "url": pr.url,
        "reason": reason,
    }


def _record_summary(
    summary: list[dict[str, Any]] | None,
    pr: PullRequest,
    status: str,
    reason: str = "",
) -> None:
    if summary is not None:
        summary.append(_summary_entry(pr, status, reason))


def _write_summary(path: Path, attempts: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    merged_codes = [
        str(attempt.get("code") or f"PR{attempt['number']}")
        for attempt in attempts
        if attempt["status"] == "merged"
    ]
    path.write_text(
        json.dumps(
            {
                "attempts": list(attempts),
                "merged_codes": merged_codes,
                "merged_code_path": "_".join(merged_codes) or "no_prs",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _merge_in_progress(repo_root: Path) -> bool:
    return (
        _git(repo_root, "rev-parse", "-q", "--verify", "MERGE_HEAD", check=False)
        .returncode
        == 0
    )


def _current_branch(repo_root: Path) -> str:
    process = _git(repo_root, "symbolic-ref", "--quiet", "--short", "HEAD", check=False)
    if process.returncode:
        return "<detached>"
    return process.stdout.strip()


def _require_clean_start(repo_root: Path, *, auto: bool = False) -> None:
    if _load_state(repo_root):
        raise WorkflowError(
            "an IFC PR merge is already active; use `git ifc pr merge --continue` "
            "or `git ifc pr merge --abort`"
        )
    if _merge_in_progress(repo_root):
        raise WorkflowError("another Git merge is already in progress")
    status = _git(repo_root, "status", "--porcelain").stdout
    if auto and status.strip():
        raise WorkflowError("`git ifc pr merge --auto` requires a clean working tree")
    # if status.strip():
    #     raise WorkflowError("working tree must be clean before starting a PR merge")


def _driver_environment(script_path: Path) -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "GIT_CONFIG_COUNT": "2",
            "GIT_CONFIG_KEY_0": "merge.ifc-xmi.name",
            "GIT_CONFIG_VALUE_0": "IFC UML structural merge",
            "GIT_CONFIG_KEY_1": "merge.ifc-xmi.driver",
            "GIT_CONFIG_VALUE_1": xmi_merge._driver_command(script_path),
        }
    )
    return env


def _commit_message(pr: PullRequest) -> str:
    source = f"{pr.head_owner}/{pr.head_ref}" if pr.head_owner else pr.head_ref
    return f"Merge pull request #{pr.number} from {source}\n\n{pr.title}"


def _replay_source_oid(repo_root: Path, pr: PullRequest, fetched_oid: str) -> str:
    """Represent only the PR delta, with an isolated base tree as its parent."""
    if not pr.base_oid:
        raise WorkflowError(f"PR #{pr.number} has no base commit")
    base_tip = pr.base_oid
    if pr.state == "MERGED":
        if not pr.merge_oid:
            raise WorkflowError(f"PR #{pr.number} has no merge commit to recover its base")
        base_tip = _git(repo_root, "rev-parse", f"{pr.merge_oid}^1").stdout.strip()
    bases = _git(repo_root, "merge-base", "--all", base_tip, fetched_oid).stdout.split()
    if len(bases) != 1:
        raise WorkflowError(f"PR #{pr.number} does not have a unique merge base")
    base_oid = bases[0]
    base_tree = _git(repo_root, "rev-parse", f"{base_oid}^{{tree}}").stdout.strip()
    base = _git(repo_root, "commit-tree", base_tree, "-m", "IFC PR replay base").stdout.strip()
    tree = _git(repo_root, "rev-parse", f"{fetched_oid}^{{tree}}").stdout.strip()
    return _git(
        repo_root, "commit-tree", tree, "-p", base, "-m", _commit_message(pr)
    ).stdout.strip()


def _merge_replay(repo_root: Path, replay_oid: str) -> subprocess.CompletedProcess[str]:
    # Give the merge an explicit base without changing preview's real ancestry.
    # The replacement is visible only to this Git invocation and its drivers.
    head = _git(repo_root, "rev-parse", "HEAD").stdout.strip()
    tree = _git(repo_root, "rev-parse", "HEAD^{tree}").stdout.strip()
    base = _git(repo_root, "rev-parse", f"{replay_oid}^").stdout.strip()
    current = _git(repo_root, "commit-tree", tree, "-p", base, "-m", "IFC preview replay").stdout.strip()
    namespace = f"refs/ifc-replay/{uuid.uuid4().hex}/"
    ref = namespace + head
    env = _driver_environment(Path(xmi_merge.__file__).resolve())
    env["GIT_REPLACE_REF_BASE"] = namespace
    _git(repo_root, "update-ref", ref, current)
    try:
        return _git(
            repo_root, "merge", "--no-commit", "--no-ff", replay_oid,
            check=False, capture=False, env=env,
        )
    finally:
        _git(repo_root, "update-ref", "-d", ref)


def _fetch_pull_request(
    repo_root: Path, remote: str, repository: str, pr: PullRequest
) -> tuple[str, PullRequest, str, str]:
    pr_ref = f"refs/ifc/pr/{pr.number}"
    _git(
        repo_root,
        "fetch",
        "--force",
        remote,
        f"+refs/pull/{pr.number}/head:{pr_ref}",
        capture=False,
    )
    fetched_oid = _git(repo_root, "rev-parse", pr_ref).stdout.strip()
    current_pr = get_pull_request(repo_root, repository, pr.number)
    if current_pr.head_oid and fetched_oid != current_pr.head_oid:
        raise WorkflowError(
            f"fetched PR #{pr.number} at {fetched_oid[:12]}, but GitHub reports "
            f"{current_pr.head_oid[:12]}; retry the merge"
        )
    if not current_pr.base_oid:
        raise WorkflowError(f"PR #{pr.number} has no base commit")
    _git(repo_root, "fetch", "--no-tags", remote, current_pr.base_oid, capture=False)
    if current_pr.state == "MERGED" and current_pr.merge_oid:
        _git(repo_root, "fetch", "--no-tags", remote, current_pr.merge_oid, capture=False)
    replay_oid = _replay_source_oid(repo_root, current_pr, fetched_oid)
    return pr_ref, current_pr, fetched_oid, replay_oid


def _unmerged_paths(repo_root: Path) -> list[str]:
    return _git(
        repo_root, "diff", "--name-only", "--diff-filter=U"
    ).stdout.splitlines()


def _unstaged_paths(repo_root: Path) -> list[str]:
    return _git(repo_root, "diff", "--name-only").stdout.splitlines()


def _is_schema_uml_path(path: str) -> bool:
    return path.startswith("schemas/") and path.endswith(".uml")


def _has_index_stage(repo_root: Path, relative_path: str, stage: int) -> bool:
    return (
        _git(
            repo_root,
            "cat-file",
            "-e",
            f":{stage}:{relative_path}",
            check=False,
        ).returncode
        == 0
    )


def _is_add_add_conflict(repo_root: Path, relative_path: str) -> bool:
    return (
        not _has_index_stage(repo_root, relative_path, 1)
        and _has_index_stage(repo_root, relative_path, 2)
        and _has_index_stage(repo_root, relative_path, 3)
    )


def _changed_schema_uml_paths(repo_root: Path, extra_paths: Sequence[str]) -> list[str]:
    paths = {path for path in extra_paths if _is_schema_uml_path(path)}
    for args in (
        ("diff", "--name-only", "--", "schemas/*.uml"),
        ("diff", "--cached", "--name-only", "--", "schemas/*.uml"),
    ):
        process = _git(repo_root, *args, check=False)
        if process.returncode == 0:
            paths.update(path for path in process.stdout.splitlines() if path)
    return sorted(paths)


def _remove_duplicate_packaged_elements(
    repo_root: Path, extra_paths: Sequence[str]
) -> tuple[bool, str, list[str]]:
    changed: list[str] = []
    for relative_path in _changed_schema_uml_paths(repo_root, extra_paths):
        path = repo_root / relative_path
        if not path.exists():
            continue
        try:
            removed = xmi_merge.remove_duplicate_xmi_id_elements(path)
        except xmi_merge.MergeConflict as exc:
            return False, str(exc), changed
        if removed:
            print(
                f"git-ifc: removed {removed} duplicate xmi:id element(s) from "
                f"{relative_path}",
                file=sys.stderr,
            )
            changed.append(relative_path)
    return True, "", changed


def _auto_resolve_conflicts(
    repo_root: Path, unmerged_paths: Sequence[str]
) -> tuple[bool, str]:
    paths_to_stage: set[str] = set()
    for relative_path in unmerged_paths:
        path = repo_root / relative_path
        if not path.exists() or path.is_dir():
            return False, f"{relative_path} is not a regular file in the worktree"
        try:
            if _is_schema_uml_path(relative_path):
                if xmi_merge.resolve_unmerged_file_by_zero_context_patches(
                    repo_root, relative_path
                ) or xmi_merge.resolve_added_file_by_structural_merge(
                    repo_root, relative_path
                ):
                    paths_to_stage.add(relative_path)
                    continue
            if not xmi_merge.has_conflict_markers(path):
                if _is_add_add_conflict(repo_root, relative_path):
                    paths_to_stage.add(relative_path)
                    continue
                return False, f"{relative_path} has no Git conflict markers to collapse"
            xmi_merge.resolve_conflict_markers_keep_both(path)
        except (OSError, xmi_merge.MergeConflict) as exc:
            return False, str(exc)
        paths_to_stage.add(relative_path)

    ok, reason, deduped_paths = _remove_duplicate_packaged_elements(
        repo_root, unmerged_paths
    )
    if not ok:
        return False, reason
    paths_to_stage.update(deduped_paths)

    if paths_to_stage:
        _git(repo_root, "add", "--", *sorted(paths_to_stage), capture=False)
    remaining = _unmerged_paths(repo_root)
    if remaining:
        return False, "auto resolution left unresolved files: " + ", ".join(remaining)
    return True, ""


def _skip_active_merge(
    repo_root: Path,
    state: MergeState,
    summary: list[dict[str, Any]] | None,
    reason: str,
) -> int:
    pr = PullRequest(**state.pull_request)
    print(f"Skipping PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}")
    if _merge_in_progress(repo_root):
        _git(repo_root, "merge", "--abort", capture=False)
    _clear_state(repo_root)
    _record_summary(summary, pr, "skipped", reason)
    return 0


def _stop_active_merge(
    state: MergeState,
    summary: list[dict[str, Any]] | None,
    reason: str,
) -> int:
    pr = PullRequest(**state.pull_request)
    print(
        f"Stopped at PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}",
        file=sys.stderr,
    )
    print(
        "The merge is left in the worktree for inspection; use "
        "`git ifc pr merge --continue --auto --stop-on-failure` after repairs "
        "or `git ifc pr merge --abort` to discard it.",
        file=sys.stderr,
    )
    _record_summary(summary, pr, "failed", reason)
    return 1


def _stop_pr_without_merge(
    pr: PullRequest,
    summary: list[dict[str, Any]] | None,
    reason: str,
) -> int:
    print(
        f"Stopped at PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}",
        file=sys.stderr,
    )
    _record_summary(summary, pr, "failed", reason)
    return 1


def _finish_merge(
    repo_root: Path,
    state: MergeState,
    *,
    auto: bool = False,
    stop_on_failure: bool = False,
    summary: list[dict[str, Any]] | None = None,
) -> int:
    pr = PullRequest(**state.pull_request)
    if not _merge_in_progress(repo_root):
        raise WorkflowError(
            "saved PR merge state exists, but Git has no MERGE_HEAD; "
            "use `git ifc pr merge --abort` to clear stale state"
        )
    current_head = _git(repo_root, "rev-parse", "HEAD").stdout.strip()
    if current_head != state.start_head:
        raise WorkflowError(
            f"HEAD changed from {state.start_head[:12]} to {current_head[:12]} "
            "while the PR merge was active"
        )
    unmerged = _unmerged_paths(repo_root)
    if unmerged:
        if auto:
            ok, reason = _auto_resolve_conflicts(repo_root, unmerged)
            if not ok:
                if stop_on_failure:
                    return _stop_active_merge(state, summary, reason)
                return _skip_active_merge(repo_root, state, summary, reason)
            unmerged = _unmerged_paths(repo_root)
        if unmerged and auto:
            reason = "auto resolution left unresolved files: " + ", ".join(unmerged)
            if stop_on_failure:
                return _stop_active_merge(state, summary, reason)
            return _skip_active_merge(
                repo_root,
                state,
                summary,
                reason,
            )
        if unmerged:
            print("PR merge still has unresolved files:", file=sys.stderr)
            for path in unmerged:
                print(f"  {path}", file=sys.stderr)
            print("Resolve and `git add` them, then run `git ifc pr merge --continue`.", file=sys.stderr)
            return 1
    if not unmerged and auto:
        ok, reason, deduped_paths = _remove_duplicate_packaged_elements(repo_root, [])
        if not ok:
            if stop_on_failure:
                return _stop_active_merge(state, summary, reason)
            return _skip_active_merge(repo_root, state, summary, reason)
        if deduped_paths:
            _git(repo_root, "add", "--", *deduped_paths, capture=False)
    unstaged = _unstaged_paths(repo_root)
    if unstaged:
        if auto:
            _git(repo_root, "add", "-A", capture=False)
            unstaged = _unstaged_paths(repo_root)
        if unstaged and auto:
            reason = "auto resolution left unstaged files: " + ", ".join(unstaged)
            if stop_on_failure:
                return _stop_active_merge(state, summary, reason)
            return _skip_active_merge(
                repo_root,
                state,
                summary,
                reason,
            )
        if unstaged:
            print("PR merge has unstaged changes:", file=sys.stderr)
            for path in unstaged:
                print(f"  {path}", file=sys.stderr)
            print("Stage them before continuing.", file=sys.stderr)
            return 1
    if xmi_merge.validate_command(repo_root):
        if auto:
            if stop_on_failure:
                return _stop_active_merge(state, summary, "validation failed")
            return _skip_active_merge(repo_root, state, summary, "validation failed")
        return 1
    _git(repo_root, "commit", "-m", state.commit_message, capture=False)
    _clear_state(repo_root)
    _record_summary(summary, pr, "merged")
    print(f"Merged PR #{pr.number}: {pr.title}")
    print("The merge commit is local; push it when ready.")
    return 0


def start_pr_merge(
    repo_root: Path,
    selector: str,
    *,
    remote_name: str | None = None,
    base: str | None = None,
    labels: Sequence[str] | None = None,
    include_drafts: bool = False,
    remaining_selectors: Sequence[str] = (),
    auto: bool = False,
    stop_on_failure: bool = False,
    summary: list[dict[str, Any]] | None = None,
) -> int:
    _require_clean_start(repo_root, auto=auto)
    remote = _remote_name(repo_root, remote_name)
    repository = _repository_name(repo_root, remote)
    configured_base = base or _config(repo_root, "ifc.base")
    pull_requests = list_pull_requests(
        repo_root,
        repository,
        base=configured_base,
        labels=labels,
        limit=1000,
        state="all",
    )
    if not include_drafts:
        pull_requests = [pr for pr in pull_requests if not pr.is_draft]
    pr = select_pull_request(pull_requests, selector)
    try:
        pr_ref, pr, fetched_oid, replay_oid = _fetch_pull_request(
            repo_root, remote, repository, pr
        )
    except WorkflowError as exc:
        if auto:
            reason = str(exc)
            if stop_on_failure:
                return _stop_pr_without_merge(pr, summary, reason)
            print(f"Skipping PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}")
            _record_summary(summary, pr, "skipped", reason)
            return 0
        raise
    print(f"Replaying PR #{pr.number} relative to its own base onto preview.")
    state = MergeState(
        version=STATE_VERSION,
        remote=remote,
        repository=repository,
        branch=_current_branch(repo_root),
        start_head=_git(repo_root, "rev-parse", "HEAD").stdout.strip(),
        pr_ref=pr_ref,
        fetched_oid=fetched_oid,
        replay_oid=replay_oid,
        commit_message=_commit_message(pr),
        started_at=datetime.now(timezone.utc).isoformat(),
        pull_request=asdict(pr),
        base=configured_base,
        include_drafts=include_drafts,
        remaining_selectors=list(remaining_selectors),
        labels=list(labels) if labels else None,
    )
    _write_state(repo_root, state)
    process = _merge_replay(repo_root, replay_oid)
    if not _merge_in_progress(repo_root):
        _clear_state(repo_root)
        if process.returncode == 0:
            if auto:
                reason = "already contained in HEAD"
                print(f"Skipping PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}")
                _record_summary(summary, pr, "skipped", reason)
                return 0
            raise WorkflowError(f"PR #{pr.number} is already contained in HEAD")
        if auto:
            reason = "Git could not start the merge"
            if stop_on_failure:
                return _stop_pr_without_merge(pr, summary, reason)
            print(f"Skipping PR #{pr.number} ({pull_request_code(pr) or pr.head_ref}): {reason}")
            _record_summary(summary, pr, "skipped", reason)
            return 0
        raise WorkflowError(f"Git could not start the merge for PR #{pr.number}")
    if process.returncode or _unmerged_paths(repo_root):
        if auto:
            return _finish_merge(
                repo_root,
                state,
                auto=True,
                stop_on_failure=stop_on_failure,
                summary=summary,
            )
        print(f"PR #{pr.number} requires manual resolution.", file=sys.stderr)
        print("Resolve and stage the conflicts, then run:", file=sys.stderr)
        print("  git ifc pr merge --continue", file=sys.stderr)
        return 1
    return _finish_merge(
        repo_root,
        state,
        auto=auto,
        stop_on_failure=stop_on_failure,
        summary=summary,
    )


def start_pr_merges(
    repo_root: Path,
    selectors: Sequence[str],
    *,
    remote_name: str | None = None,
    base: str | None = None,
    labels: Sequence[str] | None = None,
    include_drafts: bool = False,
    auto: bool = False,
    stop_on_failure: bool = False,
    summary: list[dict[str, Any]] | None = None,
) -> int:
    if not selectors:
        raise WorkflowError("provide at least one PR number, branch, or title token")
    for index, selector in enumerate(selectors):
        result = start_pr_merge(
            repo_root,
            selector,
            remote_name=remote_name,
            base=base,
            labels=labels,
            include_drafts=include_drafts,
            remaining_selectors=selectors[index + 1 :],
            auto=auto,
            stop_on_failure=stop_on_failure,
            summary=summary,
        )
        if result:
            return result
    return 0


def continue_pr_merge(
    repo_root: Path,
    *,
    auto: bool = False,
    stop_on_failure: bool = False,
    summary: list[dict[str, Any]] | None = None,
) -> int:
    state = _load_state(repo_root)
    if state is None:
        raise WorkflowError("no IFC PR merge is active")
    if _current_branch(repo_root) != state.branch:
        raise WorkflowError(
            f"merge started on branch {state.branch!r}, but current branch is "
            f"{_current_branch(repo_root)!r}"
        )
    remaining_selectors = list(state.remaining_selectors or [])
    result = _finish_merge(
        repo_root,
        state,
        auto=auto,
        stop_on_failure=stop_on_failure,
        summary=summary,
    )
    if result or not remaining_selectors:
        return result
    return start_pr_merges(
        repo_root,
        remaining_selectors,
        remote_name=state.remote,
        base=state.base,
        labels=state.labels,
        include_drafts=state.include_drafts,
        auto=auto,
        stop_on_failure=stop_on_failure,
        summary=summary,
    )


def abort_pr_merge(repo_root: Path) -> int:
    state = _load_state(repo_root)
    if state is None:
        raise WorkflowError("no IFC PR merge is active")
    if _merge_in_progress(repo_root):
        _git(repo_root, "merge", "--abort", capture=False)
    _clear_state(repo_root)
    print("Aborted IFC PR merge.")
    return 0


def install_command(repo_root: Path, remote: str | None) -> int:
    xmi_merge.install_driver(repo_root, Path(xmi_merge.__file__).resolve())
    command = " ".join(
        [
            shlex.quote(str(Path(sys.executable).resolve())),
            shlex.quote(str(Path(__file__).resolve())),
        ]
    )
    _git(repo_root, "config", "alias.ifc", f"!{command}")
    if remote:
        _remote_name(repo_root, remote)
        _git(repo_root, "config", "ifc.remote", remote)
    print("Installed `git ifc` alias.")
    print("Use `git ifc pr list` to inspect open and merged pull requests.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install", help="Install local Git aliases and drivers")
    install_parser.add_argument("--remote", help="Default GitHub remote")

    pr_parser = subparsers.add_parser("pr", help="List and merge GitHub pull requests")
    pr_subparsers = pr_parser.add_subparsers(dest="pr_command", required=True)

    list_parser = pr_subparsers.add_parser("list", help="List open and merged pull requests")
    list_parser.add_argument("--remote", help="Git remote, default: ifc.remote or origin")
    list_parser.add_argument("--base", help="Filter by GitHub base branch")
    list_parser.add_argument(
        "--label",
        action="append",
        help="Filter by GitHub label; repeat to require multiple labels",
    )
    list_parser.add_argument("--limit", type=int, default=100)
    list_parser.add_argument(
        "--state",
        choices=sorted(LIST_PR_STATES),
        default="all",
        help="PR state to list, default: all open and merged PRs",
    )
    list_parser.add_argument("--include-drafts", action="store_true")

    merge_parser = pr_subparsers.add_parser("merge", help="Merge open or merged pull requests")
    merge_parser.add_argument(
        "selectors",
        nargs="*",
        help="PR numbers, branches, or title tokens",
    )
    merge_parser.add_argument("--remote", help="Git remote, default: ifc.remote or origin")
    merge_parser.add_argument("--base", help="Filter by GitHub base branch")
    merge_parser.add_argument(
        "--label",
        action="append",
        help="Filter by GitHub label; repeat to require multiple labels",
    )
    merge_parser.add_argument(
        "--codes-only",
        action="store_true",
        help="With --all-prs, merge only PRs carrying an issue code such as [TF01]",
    )
    merge_parser.add_argument("--include-drafts", action="store_true")
    merge_parser.add_argument(
        "--auto",
        action="store_true",
        help="Resolve text conflicts by keeping both sides and drop duplicate xmi:id elements",
    )
    merge_parser.add_argument(
        "--stop-on-failure",
        action="store_true",
        help="With --auto, stop at the first failed PR instead of aborting and skipping it",
    )
    merge_parser.add_argument(
        "--all-prs",
        action="store_true",
        help="Merge all open, merged, and closed PRs sorted naturally by codes such as [TF01]",
    )
    merge_parser.add_argument(
        "--summary-json",
        type=Path,
        help="Write attempted, merged, and skipped PR details to this JSON file",
    )
    action = merge_parser.add_mutually_exclusive_group()
    action.add_argument("--continue", dest="continue_merge", action="store_true")
    action.add_argument("--abort", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = build_parser().parse_args(argv)
        repo_root = xmi_merge._repo_root()
        if args.command == "install":
            return install_command(repo_root, args.remote)
        if args.pr_command == "list":
            remote = _remote_name(repo_root, args.remote)
            repository = _repository_name(repo_root, remote)
            base = args.base or _config(repo_root, "ifc.base")
            pull_requests = list_pull_requests(
                repo_root,
                repository,
                base=base,
                labels=args.label,
                limit=args.limit,
                state=args.state,
            )
            if not args.include_drafts:
                pull_requests = [pr for pr in pull_requests if not pr.is_draft]
            _print_pull_requests(pull_requests)
            return 0
        summary: list[dict[str, Any]] | None = [] if args.summary_json else None
        if args.continue_merge:
            if args.selectors or args.all_prs:
                raise WorkflowError("do not provide selectors or --all-prs with --continue")
            result = continue_pr_merge(
                repo_root,
                auto=args.auto,
                stop_on_failure=args.stop_on_failure,
                summary=summary,
            )
            if args.summary_json:
                _write_summary(args.summary_json, summary or [])
            return result
        if args.abort:
            if args.selectors or args.all_prs:
                raise WorkflowError("do not provide selectors or --all-prs with --abort")
            return abort_pr_merge(repo_root)
        if args.all_prs:
            if args.selectors:
                raise WorkflowError("do not provide selectors with --all-prs")
            remote = _remote_name(repo_root, args.remote)
            repository = _repository_name(repo_root, remote)
            base = args.base or _config(repo_root, "ifc.base")
            pull_requests = selectable_pull_requests_by_code(
                repo_root,
                repository,
                base=base,
                labels=args.label,
                include_drafts=args.include_drafts,
            )
            if args.codes_only:
                uncoded = [pr for pr in pull_requests if pull_request_code(pr) is None]
                for pr in uncoded:
                    print(
                        f"Skipping PR #{pr.number} ({pr.title}): "
                        "no issue code such as [TF01] in title or branch"
                    )
                pull_requests = [
                    pr for pr in pull_requests if pull_request_code(pr) is not None
                ]
            if not pull_requests:
                print("No open, merged, or closed pull requests to merge.")
                if args.summary_json:
                    _write_summary(args.summary_json, summary or [])
                return 0
            print("Merging open, merged, and closed pull requests in code order:")
            for pr in pull_requests:
                code = pull_request_code(pr) or "<no-code>"
                print(f"  {code}  #{pr.number}  {pr.title}")
            result = start_pr_merges(
                repo_root,
                [str(pr.number) for pr in pull_requests],
                remote_name=remote,
                base=base,
                labels=args.label,
                include_drafts=args.include_drafts,
                auto=args.auto,
                stop_on_failure=args.stop_on_failure,
                summary=summary,
            )
            if args.summary_json:
                _write_summary(args.summary_json, summary or [])
            return result
        if not args.selectors:
            raise WorkflowError("provide at least one PR number, branch, or title token")
        result = start_pr_merges(
            repo_root,
            args.selectors,
            remote_name=args.remote,
            base=args.base,
            labels=args.label,
            include_drafts=args.include_drafts,
            auto=args.auto,
            stop_on_failure=args.stop_on_failure,
            summary=summary,
        )
        if args.summary_json:
            _write_summary(args.summary_json, summary or [])
        return result
    except WorkflowError as exc:
        print(f"git-ifc: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
