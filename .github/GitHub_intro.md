# Introduction to GitHub 

This guide explains how to contribute to buildingSMART repositories on GitHub. If you are familiar with GitHub, you do not need to read this.

GitHub is a cloud-based platform to store, manage, and collaborate primarily on technical documentation and code. However, you do not need to know how to code, use the command line or IDE editors to follow this guide. You can as well contribute using GitHub in your browser, using GitHub Desktop, or GitHub Mobile.

## Table of contents

* [How we use GitHub](#how-we-use-github)
* [Glossary](#glossary)
* [Opening an issue](#opening-an-issue)
* [Submitting changes with Pull Requests](#submitting-changes-with-pull-reqests)
* [Reviewing and commenting a pull request](#reviewing-and-commenting-a-pull-request)
* [Useful video-instructions](#useful-video-instructions)

## How we use GitHub

We use GitHub to discuss work, propose changes, review changes, and keep track of decisions.

The two most important GitHub features for contributing are:

* [Issues](https://github.com/buildingSMART/IFC4.x-development/issues): Use issues to report problems, , and suggest improvements.
* [Pull Requests](https://github.com/buildingSMART/IFC4.x-development/pulls): Use pull requests (PR), to propose a change directly in the file structure and ask others to review, so it can become a part of the project.

## Glossary

| Term                   | Definition                                                                                                                                                                          |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Repository** (Repo)  | A project stored in GitHub containing files, folders, code, documentation, issues, and history.                                                                                     |
| **Git**                | A distributed version control system used to track changes to files over time.                                                                                                      |
| **GitHub**             | A web platform for hosting Git repositories and collaborating on software and documentation projects.                                                                               |
| **Issue**              | A tracked task, bug report, feature request, question, or discussion item within a repository.                                                                                      |
| **Commit**             | A saved snapshot of changes made to a repository, accompanied by a message describing the changes.                                                                                  |
| **Pull Request** (PR)  | A proposal to merge changes from one branch into another, enabling review and discussion before integration.                                                                        |
| **Branch**             | An independent line of development that allows changes to be made without affecting the main codebase.                                                                              |
| **Main Branch**        | The primary branch of a repository, often named `main`, representing the current official version.                                                                                  |
| **Markdown**           | A lightweight text formatting language used for README files, documentation, and comments.                                                                                          |
| **README**             | The primary documentation file of a repository, typically explaining the project and how to use it.                                                                                 |
| **Label**              | A category or tag applied to issues and pull requests to aid organization and filtering.                                                                                            |
| **Discussion**         | A forum-style conversation area for broader topics that do not require formal tracking as issues.                                                                                   |
| **Review**             | The process of examining a pull request and providing feedback, approval, or requested changes.                                                                                     |
| **Release**            | A packaged and versioned snapshot of a repository, often distributed to users.                                                                                                      |
| **Commit Hash**        | A unique identifier assigned to a commit.                                                                                                                                           |
| **Fork**               | A personal copy of another user's repository that allows independent development.                                                                                                   |
| **Clone**              | A local copy of a repository downloaded from GitHub to a computer.                                                                                                                  |
| **Merge**              | The action of incorporating changes from one branch into another.                                                                                                                   |
| **Merge Conflict**     | A situation where Git cannot automatically combine changes because the same content was modified differently.                                                                       |
| **Code Contributor**   | A person who has contributed commits that are included in the repository history. In a broader sense, may also refer to people contributing reviews, documentation, or discussions. |
| **Maintainer**         | A person responsible for managing the repository, reviewing contributions and approving changes.                                                                                    |
| **Tag**                | A named reference to a specific commit, commonly used to mark releases.                                                                                                             |
| **Version**            | A numbered release of a project, such as `v1.0.0`.                                                                                                                                  |
| **Workflow**           | An automated process executed by GitHub Actions.                                                                                                                                    |
| **GitHub Actions**     | GitHub's automation platform for testing, building, and deploying projects.                                                                                                         |
| **Wiki**               | A separate documentation area within a repository.                                                                                                                                  |
| **Milestone**          | A collection of issues and pull requests grouped around a goal or release.                                                                                                          |
| **Assignee**           | A person responsible for working on a specific issue or pull request.                                                                                                               |
| **Draft Pull Request** | A pull request that is still under development and not yet ready for formal review.                                                                                                 |

## Opening an issue

Before opening a new issue, please check whether someone has already started the same discussion. Search for words related to your idea, problem, or change. If you find an existing issue or pull request, it is usually better to comment there instead of opening a duplicate.

Open an issue when you want to report something, ask a question, suggest an improvement, or start a discussion.

Good reasons to open an issue include:

* You found a bug or mistake.
* You want to suggest a new feature.
* You noticed unclear documentation.
* You want to discuss a change before working on it.

If you have general questions, it is better to use the Discussion tab. 

### How to open an issue in GitHub

1. Go to the repository on GitHub.
2. Click [Issues](https://github.com/buildingSMART/IFC4.x-development/issues).
3. Click **New issue**.
4. Choose the most relevant issue type or template, if templates are available.
5. Write a clear title.
6. Add details in the description.
7. Add screenshots, links, or examples if they help explain the issue.
8. Click **Submit new issue**.

### How to write a useful issue

A good issue helps other people understand the situation quickly. Include:
- A clear problem statement
- The proposed solution(s), with their rationale
- Any relevant context
- Examples, screenshots can be useful too

## Commenting on an issue

Before commenting, read the existing discussion so you do not repeat something that has already been answered.

## Submitting changes with Pull Requests

### Edit or Fork

Changes can be proposed directly from the GitHub website by clicking **Edit** button, or by submitting it from your local repository. To create a local repository, you need to **Fork** it first. 

### Create new branch

2. Create a new branch


### Openning a Pull Request

Once your changes are ready, you can submit them for review through **Pull Request**. You can do that from console, but also from the GitHub website.  

A pull request is a proposed change. It lets other people look at your work, ask questions, suggest edits, and decide whether the change should be accepted. Some repositories have automated tests that verify quality and that nothing breaks.

Small PRs are easier to review than very large PRs. If your change covers many unrelated topics, consider opening separate PRs.

Good reasons to open a pull request include:

* You fixed a typo or documentation problem.
* You updated a file.
* You improved a feature.
* You fixed a bug.

The exact steps may depend on how you made your change, but the general process is:

1. Go to the repository on GitHub.
1. Open the **Pull requests** tab.
1. Click **New pull request**.
1. Choose the branch or change you want to propose.
1. Review the list of changed files.
1. Write a clear title.
1. Fill in the PR description. A good PR description explains what changed and why, but most importantly it **links the issue that is resolving** For example: `Closes #123`
1. Add screenshots or notes, if helpful.
1. Click **Create pull request**.

Remember to check:

* Is there an issue related to this change?
* Does the change solve the problem described in the issue and nothing else?
* Did you explain what changed and why?


## Reviewing and commenting a Pull Request

There are two common ways to comment on a PR. Use a **general comment** when your feedback is about the whole PR. Use a **line comment** when your feedback is about a specific line or part of a file.

Reviewing a PR means checking a proposed change before it is accepted.

You do not need to understand every technical detail to be helpful. You can still review for clarity, wording, user experience, screenshots, broken links, missing context, or whether the change solves the issue.

1. Open the **Pull requests** tab.
1. Read the PR title and description.
1. Check whether a related issue is linked.
1. Open the **Conversation** tab to understand the discussion.
1. Open the **Files changed** tab to see what changed - added, removed, or edited.
	* Green lines usually show content that was added.
	* Red lines usually show content that was removed.
	* The file list shows which files were changed.
	* You can comment on a specific line if your feedback is about that exact part.
	* You can mark files as viewed to keep track of what you already checked.
1. Look at one file at a time.
1. Leave comments where needed.
1. Choose **Comment**, **Approve**, or **Request changes**.

Depending on the type of change, you can check:

* Does this solve the issue?
* Is the explanation clear?
* Are there typos or broken links?
* Is anything confusing or missing?
* Is the change too large or trying to solve too many things at once?

When you finish reviewing a PR, GitHub may ask you to choose one of these options:
* **Comment** when you want to leave feedback, but you are not approving or blocking the PR.
* **Approve** when the change looks ready from your point of view.
* **Request changes** when something must be fixed before the PR should be accepted.


## Useful video-instructions

* [How to use GitHub issues and projects](https://www.youtube.com/watch?v=c67GaAkf1BE)
* [How to create a pull request in 4 min](https://www.youtube.com/watch?v=nCKdihvneS0)
* [How to Review a Pull Request in GitHub the RIGHT Way](https://www.youtube.com/watch?v=lSnbOtw4izI)
* [5 Tips for Reviewing a GitHub Pull Request](https://www.youtube.com/watch?v=nP9Y72HQNaA)
