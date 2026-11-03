import json
from pathlib import Path

import pytest

from tools import git_ifc
from tools.git_ifc import MergeState, PullRequest, WorkflowError


def completed(stdout="", returncode=0, stderr=""):
    return type(
        "Result",
        (),
        {"stdout": stdout, "stderr": stderr, "returncode": returncode},
    )()


def gh_pr_value(number, state="OPEN", *, updated_at=None):
    updated_at = updated_at or f"2026-06-{number:02d}T00:00:00Z"
    return {
        "number": number,
        "title": f"PR {number}",
        "headRefName": f"content/pr-{number}",
        "headRefOid": f"{number:040x}",
        "headRepositoryOwner": {"login": "owner"},
        "baseRefName": "main",
        "baseRefOid": "b" * 40,
        "isDraft": False,
        "state": state,
        "url": f"https://example.test/pull/{number}",
        "author": {"login": "author"},
        "updatedAt": updated_at,
        "mergedAt": "2026-06-14T00:00:00Z" if state == "MERGED" else None,
    }


def pr(number, head, title, *, draft=False, pr_state="OPEN", base_oid=None):
    return PullRequest(
        number=number,
        title=title,
        head_ref=head,
        head_oid=f"{number:040x}",
        head_owner="owner",
        base_ref="main",
        base_oid=base_oid or "b" * 40,
        is_draft=draft,
        state=pr_state,
        url=f"https://example.test/pull/{number}",
        author="author",
        updated_at="2026-06-15T00:00:00Z",
        merged_at="2026-06-14T00:00:00Z" if pr_state == "MERGED" else None,
    )


def state():
    pull_request = pr(12, "content/tf01", "[TF01] Foundations")
    return MergeState(
        version=git_ifc.STATE_VERSION,
        remote="origin",
        repository="owner/repo",
        branch="main",
        start_head="a" * 40,
        pr_ref="refs/ifc/pr/12",
        fetched_oid=pull_request.head_oid,
        replay_oid=pull_request.head_oid,
        commit_message="Merge PR",
        started_at="2026-06-15T00:00:00+00:00",
        pull_request=git_ifc.asdict(pull_request),
        base="main",
        include_drafts=False,
        remaining_selectors=[],
    )


def test_selects_by_number_branch_and_title_token():
    pull_requests = [
        pr(12, "content/tf01", "[TF01] Foundations"),
        pr(13, "tm02", "[TM02] Something else"),
    ]

    assert git_ifc.select_pull_request(pull_requests, "#12").number == 12
    assert git_ifc.select_pull_request(pull_requests, "TF01").number == 12
    assert git_ifc.select_pull_request(pull_requests, "content/tf01").number == 12


def test_rejects_ambiguous_selector():
    pull_requests = [
        pr(12, "content/tf01", "[TF01] Foundations"),
        pr(13, "review/tf01", "[TF01] Alternative"),
    ]

    with pytest.raises(WorkflowError, match="multiple"):
        git_ifc.select_pull_request(pull_requests, "TF01")


def test_lists_all_selectable_pull_requests_by_default(tmp_path, monkeypatch):
    seen_states = []

    def fake_run(command, _repo, **_kwargs):
        gh_state = command[command.index("--state") + 1]
        seen_states.append(gh_state)
        assert gh_state == "all"
        values = [
            gh_pr_value(12, "OPEN", updated_at="2026-06-12T00:00:00Z"),
            gh_pr_value(10, "MERGED", updated_at="2026-06-10T00:00:00Z"),
            gh_pr_value(9, "CLOSED", updated_at="2026-06-09T00:00:00Z"),
        ]
        return completed(stdout=json.dumps(values))

    monkeypatch.setattr(git_ifc, "_run", fake_run)

    pull_requests = git_ifc.list_pull_requests(tmp_path, "owner/repo")

    assert seen_states == ["all"]
    assert [(pr.number, pr.state) for pr in pull_requests] == [
        (12, "OPEN"),
        (10, "MERGED"),
        (9, "CLOSED"),
    ]


def test_list_state_filter_only_queries_requested_state(tmp_path, monkeypatch):
    seen_states = []

    def fake_run(command, _repo, **_kwargs):
        gh_state = command[command.index("--state") + 1]
        seen_states.append(gh_state)
        return completed(stdout=json.dumps([gh_pr_value(10, "MERGED")]))

    monkeypatch.setattr(git_ifc, "_run", fake_run)

    pull_requests = git_ifc.list_pull_requests(
        tmp_path, "owner/repo", state="merged"
    )

    assert seen_states == ["merged"]
    assert pull_requests[0].state == "MERGED"


def test_print_pull_requests_includes_state(capsys):
    git_ifc._print_pull_requests(
        [
            pr(12, "content/tf01", "[TF01] Foundations"),
            pr(10, "content/tm10", "[TM10] Earlier", pr_state="MERGED"),
        ]
    )

    output = capsys.readouterr().out
    assert "STATE" in output
    assert "OPEN" in output
    assert "MERGED" in output


def test_sorts_pull_requests_by_bracketed_code_naturally():
    pull_requests = [
        pr(12, "content/tf10", "[TF10] Later"),
        pr(13, "content/tm01", "[TM01] Other group"),
        pr(14, "content/tf02", "[TF2] Middle"),
        pr(15, "content/tf01", "[TF01] First"),
    ]

    ordered = git_ifc.sort_pull_requests_by_code(pull_requests)

    assert [git_ifc.pull_request_code(pr) for pr in ordered] == [
        "TF01",
        "TF2",
        "TF10",
        "TM01",
    ]


@pytest.mark.parametrize("conflict", [False, True])
@pytest.mark.parametrize("merged", [False, True])
def test_replays_only_pr_delta_with_real_git(tmp_path, conflict, merged):
    import subprocess
    from dataclasses import replace

    def git(*args):
        return subprocess.check_output(["git", *args], cwd=tmp_path, text=True).strip()

    git("init")
    git("config", "user.name", "Test")
    git("config", "user.email", "test@example.test")
    (tmp_path / "workflow.yml").write_text("original\n")
    (tmp_path / "content.md").write_text("original\n")
    git("add", ".")
    git("commit", "-m", "common")
    git("branch", "preview")
    (tmp_path / "workflow.yml").write_text("main infrastructure\n")
    git("commit", "-am", "main infrastructure")
    base = git("rev-parse", "HEAD")
    (tmp_path / "content.md").write_text("PR content\n")
    git("commit", "-am", "topic")
    topic = git("rev-parse", "HEAD")
    # Advancing the base after the PR branched must not replay base changes.
    git("checkout", "-b", "advanced-base", base)
    (tmp_path / "later.py").write_text("main only\n")
    git("add", ".")
    git("commit", "-m", "later main")
    base = git("rev-parse", "HEAD")
    merge_oid = ""
    if merged:
        git("merge", "--no-ff", topic, "-m", "merged PR into main")
        merge_oid = git("rev-parse", "HEAD")
        base = merge_oid
    git("checkout", "preview")
    (tmp_path / "workflow.yml").write_text("preview infrastructure\n")
    if conflict:
        (tmp_path / "content.md").write_text("preview content\n")
    git("commit", "-am", "preview infrastructure")
    head = git("rev-parse", "HEAD")
    request = replace(
        pr(20, "topic", "[TC20] Topic"), base_oid=base,
        state="MERGED" if merged else "OPEN", merge_oid=merge_oid,
    )
    replay = git_ifc._replay_source_oid(tmp_path, request, topic)
    result = git_ifc._merge_replay(tmp_path, replay)
    assert result.returncode == (1 if conflict else 0)
    assert (tmp_path / "workflow.yml").read_text() == "preview infrastructure\n"
    assert not (tmp_path / "later.py").exists()
    assert git("rev-parse", "HEAD") == head
    assert not git("for-each-ref", "refs/ifc-replay")
    if conflict:
        assert git("diff", "--name-only", "--diff-filter=U") == "content.md"
        git("merge", "--abort")
        assert (tmp_path / "content.md").read_text() == "preview content\n"
    else:
        assert (tmp_path / "content.md").read_text() == "PR content\n"
        git("commit", "-m", "replayed")
        assert git("rev-parse", "HEAD^1") == head
        assert git("diff", "--name-only", "HEAD^1", "HEAD") == "content.md"


def test_fetch_pull_request_accepts_missing_closed_head_oid(tmp_path, monkeypatch):
    pull_request = pr(
        20,
        "content/tm20",
        "[TM20] Full",
        pr_state="CLOSED",
        base_oid="b" * 40,
    )
    current = PullRequest(
        **{
            **git_ifc.asdict(pull_request),
            "head_oid": "",
        }
    )
    commands = []

    def fake_git(_repo, *args, **kwargs):
        commands.append(args)
        if args[0] == "fetch":
            return completed()
        if args == ("rev-parse", "refs/ifc/pr/20"):
            return completed(stdout="d" * 40 + "\n")
        if args == ("show", "-s", "--format=%P", "d" * 40):
            return completed(stdout="c" * 40 + "\n")
        raise AssertionError(args)

    monkeypatch.setattr(git_ifc, "_git", fake_git)
    monkeypatch.setattr(git_ifc, "get_pull_request", lambda *_args: current)
    monkeypatch.setattr(git_ifc, "_replay_source_oid", lambda *_args: "d" * 40)

    assert git_ifc._fetch_pull_request(
        tmp_path, "origin", "owner/repo", pull_request
    ) == (
        "refs/ifc/pr/20",
        current,
        "d" * 40,
        "d" * 40,
    )


def test_parser_accepts_multiple_merge_selectors():
    args = git_ifc.build_parser().parse_args(["pr", "merge", "tf02", "tf03"])

    assert args.selectors == ["tf02", "tf03"]


def test_parser_accepts_auto_all_prs_summary():
    args = git_ifc.build_parser().parse_args(
        [
            "pr",
            "merge",
            "--auto",
            "--stop-on-failure",
            "--all-prs",
            "--summary-json",
            "summary.json",
        ]
    )

    assert args.auto is True
    assert args.stop_on_failure is True
    assert args.all_prs is True
    assert args.summary_json == Path("summary.json")


def test_start_pr_merges_processes_selectors_in_order(tmp_path, monkeypatch):
    seen = []

    def fake_start_pr_merge(_repo, selector, **kwargs):
        seen.append(
            (
                selector,
                kwargs["remote_name"],
                kwargs["base"],
                kwargs["include_drafts"],
                tuple(kwargs["remaining_selectors"]),
            )
        )
        return 0

    monkeypatch.setattr(git_ifc, "start_pr_merge", fake_start_pr_merge)

    assert (
        git_ifc.start_pr_merges(
            tmp_path,
            ["tf02", "tf03"],
            remote_name="upstream",
            base="ifc4.4-main",
            include_drafts=True,
        )
        == 0
    )
    assert seen == [
        ("tf02", "upstream", "ifc4.4-main", True, ("tf03",)),
        ("tf03", "upstream", "ifc4.4-main", True, ()),
    ]


def test_start_pr_merges_stops_on_first_nonzero_result(tmp_path, monkeypatch):
    seen = []

    def fake_start_pr_merge(_repo, selector, **_kwargs):
        seen.append(selector)
        return 1

    monkeypatch.setattr(git_ifc, "start_pr_merge", fake_start_pr_merge)

    assert git_ifc.start_pr_merges(tmp_path, ["tf02", "tf03"]) == 1
    assert seen == ["tf02"]


def test_continue_resumes_remaining_selectors(tmp_path, monkeypatch):
    expected = state()
    expected.remaining_selectors = ["tf03", "tf04"]
    expected.base = "ifc4.4-main"
    expected.include_drafts = True
    seen = []

    monkeypatch.setattr(git_ifc, "_load_state", lambda _repo: expected)
    monkeypatch.setattr(git_ifc, "_current_branch", lambda _repo: "main")
    monkeypatch.setattr(git_ifc, "_finish_merge", lambda _repo, _state, **_kwargs: 0)

    def fake_start_pr_merges(_repo, selectors, **kwargs):
        seen.append(
            (
                list(selectors),
                kwargs["remote_name"],
                kwargs["base"],
                kwargs["include_drafts"],
            )
        )
        return 0

    monkeypatch.setattr(git_ifc, "start_pr_merges", fake_start_pr_merges)

    assert git_ifc.continue_pr_merge(tmp_path) == 0
    assert seen == [(["tf03", "tf04"], "origin", "ifc4.4-main", True)]


def test_merge_state_round_trip(tmp_path, monkeypatch):
    state_path = tmp_path / "state.json"
    monkeypatch.setattr(git_ifc, "_state_path", lambda _repo: state_path)

    expected = state()
    git_ifc._write_state(tmp_path, expected)

    assert git_ifc._load_state(tmp_path) == expected
    git_ifc._clear_state(tmp_path)
    assert git_ifc._load_state(tmp_path) is None


def test_remote_name_prefers_argument_then_config(tmp_path, monkeypatch):
    seen = []
    monkeypatch.setattr(git_ifc, "_config", lambda _repo, _key: "configured")
    monkeypatch.setattr(
        git_ifc,
        "_git",
        lambda _repo, *args, **kwargs: (
            seen.append(args)
            or type("Result", (), {"returncode": 0, "stdout": "url\n"})()
        ),
    )

    assert git_ifc._remote_name(tmp_path, "explicit") == "explicit"
    assert seen[-1] == ("remote", "get-url", "explicit")
    assert git_ifc._remote_name(tmp_path, None) == "configured"
    assert seen[-1] == ("remote", "get-url", "configured")


def test_continue_defers_while_files_are_unmerged(tmp_path, monkeypatch, capsys):
    expected = state()
    monkeypatch.setattr(git_ifc, "_load_state", lambda _repo: expected)
    monkeypatch.setattr(git_ifc, "_current_branch", lambda _repo: "main")
    monkeypatch.setattr(git_ifc, "_merge_in_progress", lambda _repo: True)
    monkeypatch.setattr(
        git_ifc,
        "_git",
        lambda _repo, *args, **kwargs: type(
            "Result", (), {"stdout": expected.start_head + "\n"}
        )(),
    )
    monkeypatch.setattr(git_ifc, "_unmerged_paths", lambda _repo: ["schemas/A.uml"])

    assert git_ifc.continue_pr_merge(tmp_path) == 1
    assert "schemas/A.uml" in capsys.readouterr().err


def test_finish_does_not_commit_when_validation_fails(tmp_path, monkeypatch):
    expected = state()
    commands = []
    monkeypatch.setattr(git_ifc, "_merge_in_progress", lambda _repo: True)
    monkeypatch.setattr(git_ifc, "_unmerged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc, "_unstaged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc.xmi_merge, "validate_command", lambda _repo: 1)
    monkeypatch.setattr(
        git_ifc,
        "_git",
        lambda _repo, *args, **kwargs: (
            type("Result", (), {"stdout": expected.start_head + "\n"})()
            if args == ("rev-parse", "HEAD")
            else commands.append(args)
        ),
    )

    assert git_ifc._finish_merge(tmp_path, expected) == 1
    assert commands == []


def test_auto_finish_aborts_and_records_skip_when_validation_fails(tmp_path, monkeypatch):
    expected = state()
    commands = []
    cleared = []
    summary = []
    monkeypatch.setattr(git_ifc, "_merge_in_progress", lambda _repo: True)
    monkeypatch.setattr(git_ifc, "_unmerged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc, "_unstaged_paths", lambda _repo: [])
    monkeypatch.setattr(
        git_ifc,
        "_remove_duplicate_packaged_elements",
        lambda _repo, _paths: (True, "", []),
    )
    monkeypatch.setattr(git_ifc.xmi_merge, "validate_command", lambda _repo: 1)

    def fake_git(_repo, *args, **_kwargs):
        if args == ("rev-parse", "HEAD"):
            return completed(stdout=expected.start_head + "\n")
        commands.append(args)
        return completed()

    monkeypatch.setattr(git_ifc, "_git", fake_git)
    monkeypatch.setattr(git_ifc, "_clear_state", lambda _repo: cleared.append(True))

    assert git_ifc._finish_merge(tmp_path, expected, auto=True, summary=summary) == 0
    assert ("merge", "--abort") in commands
    assert cleared == [True]
    assert summary[0]["status"] == "skipped"
    assert summary[0]["reason"] == "validation failed"


def test_auto_stop_on_failure_leaves_merge_for_inspection(tmp_path, monkeypatch):
    expected = state()
    commands = []
    cleared = []
    summary = []
    monkeypatch.setattr(git_ifc, "_merge_in_progress", lambda _repo: True)
    monkeypatch.setattr(git_ifc, "_unmerged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc, "_unstaged_paths", lambda _repo: [])
    monkeypatch.setattr(
        git_ifc,
        "_remove_duplicate_packaged_elements",
        lambda _repo, _paths: (True, "", []),
    )
    monkeypatch.setattr(git_ifc.xmi_merge, "validate_command", lambda _repo: 1)

    def fake_git(_repo, *args, **_kwargs):
        if args == ("rev-parse", "HEAD"):
            return completed(stdout=expected.start_head + "\n")
        commands.append(args)
        return completed()

    monkeypatch.setattr(git_ifc, "_git", fake_git)
    monkeypatch.setattr(git_ifc, "_clear_state", lambda _repo: cleared.append(True))

    assert (
        git_ifc._finish_merge(
            tmp_path,
            expected,
            auto=True,
            stop_on_failure=True,
            summary=summary,
        )
        == 1
    )
    assert ("merge", "--abort") not in commands
    assert cleared == []
    assert summary[0]["status"] == "failed"
    assert summary[0]["reason"] == "validation failed"


def test_finish_commits_and_clears_state(tmp_path, monkeypatch):
    expected = state()
    commands = []
    cleared = []
    monkeypatch.setattr(git_ifc, "_merge_in_progress", lambda _repo: True)
    monkeypatch.setattr(git_ifc, "_unmerged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc, "_unstaged_paths", lambda _repo: [])
    monkeypatch.setattr(git_ifc.xmi_merge, "validate_command", lambda _repo: 0)
    monkeypatch.setattr(
        git_ifc,
        "_git",
        lambda _repo, *args, **kwargs: (
            type("Result", (), {"stdout": expected.start_head + "\n"})()
            if args == ("rev-parse", "HEAD")
            else commands.append(args)
        ),
    )
    monkeypatch.setattr(git_ifc, "_clear_state", lambda _repo: cleared.append(True))

    assert git_ifc._finish_merge(tmp_path, expected) == 0
    assert commands == [("commit", "-m", "Merge PR")]
    assert cleared == [True]


def test_abort_does_not_touch_unrelated_merge(tmp_path, monkeypatch):
    monkeypatch.setattr(git_ifc, "_load_state", lambda _repo: None)
    commands = []
    monkeypatch.setattr(
        git_ifc, "_git", lambda _repo, *args, **kwargs: commands.append(args)
    )

    with pytest.raises(WorkflowError, match="no IFC PR merge"):
        git_ifc.abort_pr_merge(tmp_path)
    assert commands == []
