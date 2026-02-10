
---

# Team Git Workflow Guidelines

This repository uses a two-branch workflow to keep work organized, stable, and easy to review.

## Branches

**main**
Stable branch used for demos and final submissions.
Protected: pull requests only.

**development**
Integration branch where all work is merged first.
Protected: pull requests only.

Direct pushes to `main` or `development` are restricted.

---

## One-time setup (everyone)

Configure your Git identity so individual contributions are visible:

```
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"
```

---

## Daily workflow

### 1. Sync `development` before starting work

```
git switch development
git pull --ff-only
```

### 2. Switch to a feature branch

If continuing work on an existing feature branch
```
git switch <feature-branch>
```

If starting work on a new feature branch
```
git switch -c <feature-branch>
```
Branch naming guidelines:

* Use 1-3 words
* Use lowercase letters only
* Separate words with hyphens

Valid examples:
* `result-page`
* `survival-model-tuning`

### 3. Make changes and commit

Commit as often as makes sense.

```
git add -A
git commit -m "Clear description of change"
```

---

## Commit message guidelines

Use [Chris Beams' seven rules](https://chris.beams.io/git-commit#seven-rules) as the required standard to keep the history readable and consistent.

Short version:

* Start with a capital letter.
* Do not include a trailing period.
* Keep it to one concise line.

Examples:

```
Add contribution guidelines
Handle missing passenger age
Add survival prediction endpoint
```

### 4. Sync again before pushing

This reduces conflicts.

```
git switch development
git pull --ff-only
git switch <feature-branch>
git merge development
```

### 5. Push and open a pull request (PR)

If working on a new feature branch, set upstream
```
git push --set-upstream origin <feature-branch>
```
If branch already exists upstream
```
git push -u origin <feature-branch>
```

Open a pull request from `<feature-branch>` to `development`.

Add an explanation of what the pull request does in the form "This pull request..." to give the team a quick overview of the changes.

---

## Pull request guidelines

* Check PRs a few times a day, and aim to leave a first review within 3-4 working hours.
* When you have created a PR, inform the team in the team chat with the PR title and link.
* When reviewing a PR, inform the team by reacting to the PR message with :raisedhand: and assign yourself to the pull request in GitHub.
* After 1 approval and passing checks, the PR author merges. If the author is unavailable for 1-2 working hours, the approving reviewer may merge.
* Merge method: **Create a merge commit** (do not squash).
  This preserves the full commit history for each contributor.

---

## Releases (`development` → `main`)

Only merge to `main` at agreed milestones (demos, checkpoints, final submission).

1. Open a pull request from `development` to `main`.
2. Merge using **Create a merge commit**.
3. Immediately open a pull request from `main` back to `development` and merge it.
   This keeps `development` in sync with `main`.

---

## Hard rules

* Always run `git pull --ff-only` before starting work
* Always pull and merge the latest changes from `development` before pushing.
* Never rebase `development` or `main`.
* If `git pull --ff-only` fails, stop and ask for help before proceeding.

Following these rules keeps the history clear, avoids unnecessary conflicts, and ensures contributions are easy to review.
