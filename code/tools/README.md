# IFC UML merge tool

`xmi_merge.py` provides a conservative structural merge driver for the UML/XMI
files in `schemas/`.

## Installation

Install the structural merge driver and the `git ifc` recurring command:

```powershell
python code/tools/git_ifc.py install --remote origin
```

The remote is stored as the local Git setting `ifc.remote`. Override it for one
command with `--remote`, or change it later:

```powershell
git config ifc.remote upstream
```

The installation creates:

- A local `merge.ifc-xmi` Git merge driver.
- A local `git ifc` alias pointing at `git_ifc.py`.
- The tracked `.gitattributes` association for `schemas/*.uml`.

## Pull-request workflow

List open and already merged pull requests from the GitHub repository
represented by the selected Git remote:

```powershell
git ifc pr list
git ifc pr list --remote upstream
git ifc pr list --base ifc4.4-main
git ifc pr list --state merged
```

Merge one or more PRs by number, exact branch name, branch basename, or an
unambiguous title token:

```powershell
git ifc pr merge 23
git ifc pr merge content/tf01
git ifc pr merge TF01
git ifc pr merge tf02 tf03
```

The command:

1. Requires a clean worktree and no existing merge.
2. Resolves the GitHub repository from the configured Git remote using `gh`.
3. Fetches `refs/pull/<number>/head` into `refs/ifc/pr/<number>` and fetches its base.
4. Records the exact PR head OID and merge state under `.git`.
5. Replays the PR diff from its merge base onto the current branch using
   `git merge --no-commit --no-ff` with the structural UML driver.
6. Validates all UML, duplicate `xmi:id` values, and EXPRESS generation.
7. Creates a local merge commit when validation succeeds.

It does not push the resulting commit.

The replay uses the PR's own base branch, rather than the common ancestor
between preview and the PR. Changes inherited from the base branch are therefore
excluded, while edits made by the PR (including conflict resolutions) are retained.
There is no file-extension filter: a PR's own code changes are replayed too.

The local merge has the existing branch tip as its first parent and a synthetic
PR snapshot as its second parent. The snapshot has an isolated base-tree parent,
so it does not import the source branch's infrastructure history. A temporary,
invocation-scoped Git replacement supplies this base to the merge and is removed
before validation or user conflict resolution. Normal continue and abort commands
still apply.

Merged PRs are included so a fresh reconstruction branch can replay work that
GitHub already marked merged. Their base is recovered from the first parent of
the GitHub merge commit, before the PR was integrated; this prevents an already
merged PR from appearing to have an empty diff against today's base branch.

If Git, the structural driver, or the generator requires user intervention,
resolve and stage the files before continuing:

```powershell
git status
git add <resolved-files>
git ifc pr merge --continue
```

For a multi-PR command, `--continue` resumes the queued selectors after the
active PR merge is committed.

Abort only the active IFC PR merge with:

```powershell
git ifc pr merge --abort
```

Draft PRs are omitted by default. Add `--include-drafts` to list or merge them.
Closed, unmerged PRs are intentionally excluded from this workflow.

## Reopening closed pull requests

`reopen_prs.py` reopens every closed, unmerged PR for a selected Git remote.
The default invocation is a dry run:

```powershell
python code/tools/reopen_prs.py origin
python code/tools/reopen_prs.py upstream --base ifc4.4-main
```

Execute the displayed plan interactively:

```powershell
python code/tools/reopen_prs.py origin --execute
```

For non-interactive execution, explicit confirmation is required:

```powershell
python code/tools/reopen_prs.py origin --execute --yes
```

An optional reopening comment can be applied to every eligible PR:

```powershell
python code/tools/reopen_prs.py origin --execute --yes `
  --comment "Reopened for reconstruction with the structural merge workflow."
```

GitHub does not allow a merged PR to be reopened. The script reports merged PRs
separately and skips them. It continues after an individual reopen failure,
prints a final success/failure count, and exits nonzero when any reopen fails.

## Recommended usage

For a branch or commit that is not represented by a GitHub PR, use the lower
level merge wrapper:

```powershell
python code/tools/xmi_merge.py merge <branch-or-commit>
```

The wrapper:

1. Requires a clean worktree.
2. Runs `git merge --no-commit --no-ff` with the structural UML driver.
3. Parses every `schemas/*.uml` file.
4. Rejects duplicate `xmi:id` values within a UML document.
5. Runs `python -m generators.express ../schemas/ifc4x3_add2.uml`.
6. Leaves the merge uncommitted for review.

When validation succeeds, review and commit normally:

```powershell
git status
git diff --cached
git commit
```

When the tool cannot prove a merge safe, it exits nonzero and leaves the merge
for manual resolution. After editing the unresolved result, rerun:

```powershell
python code/tools/xmi_merge.py validate
```

Abort the merge with `git merge --abort` when the combined change is not
appropriate.

## Ordinary Git merges

To install only the file-level driver in this repository's local Git
configuration:

```powershell
python code/tools/xmi_merge.py install
```

The tracked `.gitattributes` file associates `schemas/*.uml` with that driver.
An ordinary `git merge` will then use structural UML merging, but it will not
run the repository-wide EXPRESS check. Use the wrapper for the full validation
workflow.

## Merge policy

The driver merges complete XML elements, primarily identified by `xmi:id`.
One-sided edits, independent additions, and identical additions are accepted.
It defers to the user for cases including:

- Different additions using the same `xmi:id`.
- Duplicate IDs in any input or result document.
- Two-sided edits to the same leaf value.
- Delete/modify conflicts.
- Incompatible element ordering.
- Mixed XML/text content that cannot be reconstructed without guessing.
- Malformed XML or a failing EXPRESS generator.

The implementation preserves raw element bytes instead of serializing the
entire XML tree. This avoids broad formatting, namespace, and entity-escaping
changes in otherwise untouched UML content.
