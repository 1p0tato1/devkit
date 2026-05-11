# 🛠️ devkit

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-FF6B6B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A modern developer toolkit that brings GitHub, Git, and AI directly into your terminal.**

[Getting Started](#-getting-started) · [Features](#-features--command-showcase) · [Live Demo](#-live-demo) · [Commands](#-features--command-showcase)

</div>

---

## 📖 Project Description

`devkit` is a modern Command Line Interface (CLI) tool built to **supercharge developer workflows**. Instead of juggling multiple tabs, browser windows, and tools, `devkit` brings everything you need into a single, unified terminal experience.

### Why devkit?

Modern software development involves constantly switching contexts: checking GitHub issues, reviewing pull requests, writing commit messages, starting feature branches, and understanding complex commands. Each of these tasks traditionally requires separate tools or manual steps.

`devkit` solves this by integrating:

- **🐙 GitHub CLI (`gh`)** — Query issues, pull requests, and repository data without leaving the terminal.
- **🌿 Git** — Automate repetitive branching and commit workflows with intelligent defaults.
- **🤖 AI Tools** — Leverage **Claude**, **Gemini**, and **GitHub Copilot** to review code, generate commit messages, plan features, and explain commands — all from one place.

Built with **Python**, powered by **Typer** for a clean CLI experience, and styled with **Rich** for beautiful, readable terminal output — `devkit` is designed to be both powerful and a pleasure to use.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python **3.10** or higher
- `git`
- GitHub CLI (`gh`) — [Installation guide](https://cli.github.com/)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/1p0tato1/devkit.git
cd devkit
```

**2. Create and activate a virtual environment**

```bash
# Create the virtual environment
python -m venv .venv

# Activate it — macOS/Linux
source .venv/bin/activate

# Activate it — Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

**3. Install devkit in editable mode**

```bash
pip install -e .
```

**4. Verify the installation**

```bash
devkit --help
```

You should see the `devkit` help menu with all available commands. You're ready to go! ✅

---

## 🎬 Live Demo

See `devkit` in action with a full end-to-end terminal recording:

https://github.com/1p0tato1/devkit/raw/main/video-demo.mp4

---

## ✨ Features & Command Showcase

`devkit` is organized into two main command groups:

| Group | Purpose |
|---|---|
| `devkit gh` | GitHub integration — issues, PRs, repository data |
| `devkit ai` | AI-powered tools — review, commit, explain |
| `devkit workflow` | Automated Git + GitHub workflows |

---

### 1️⃣ `devkit gh issues` — List GitHub Issues

Instantly fetch and display all open issues for the current repository. No browser required.

```bash
$ devkit gh issues
#1 Ma première issue
```

**Why it's useful:** Get a quick overview of open work items directly in your terminal, keeping you in the flow without context switching.

---

### 2️⃣ `devkit ai review <pr_number>` — AI-Powered PR Review

Fetch the diff of any pull request and have an AI model (Claude by default) analyze it, providing an instant code review summary.

```bash
$ devkit ai review 5
⠹ Fetching PR diff...
╭──────────────────────── AI Review (claude) — PR #5 ────────────────────────╮
│ Simulation de Claude : Plan d'action genere avec succes.                   │
╰────────────────────────────────────────────────────────────────────────────╯
```

**Why it's useful:** Get an immediate second opinion on pull requests before merging. The AI highlights potential issues, summarizes changes, and helps maintain code quality — in seconds.

---

### 3️⃣ `devkit workflow feature-start` — Start a Feature Branch

Automate the entire feature-start workflow in one command: create a properly named branch, open a Draft PR on GitHub, and generate an AI implementation plan — all at once.

```bash
$ devkit workflow feature-start "demo-finale" --issue 2
─────────────────────────────── Starting Feature ───────────────────────────────
✓ Created branch: feature/demo-finale
✓ Draft PR created: https://github.com/1p0tato1/devkit/pull/5
╭────────────────────────── AI Implementation Plan ──────────────────────────╮
│ Simulation de Claude : Plan d'action genere avec succes.                   │
╰────────────────────────────────────────────────────────────────────────────╯
──────────────────────────────── Ready to code! ────────────────────────────────
```

**Why it's useful:** Eliminates the repetitive boilerplate of starting a new feature: no more manually typing `git checkout -b`, `git push`, and then opening a PR in the browser. One command does it all, and you even get an AI-generated plan to guide your implementation.

---

### 4️⃣ `devkit ai commit` — AI-Generated Commit Messages

Let the AI analyze your staged changes and suggest a meaningful, conventional commit message. You stay in control — just confirm or reject the suggestion.

```bash
$ devkit ai commit
╭──────────────────────── Suggested Message (claude) ────────────────────────╮
│ Simulation de Claude : Plan d'action genere avec succes.                   │
╰────────────────────────────────────────────────────────────────────────────╯
Use this message? [y/n]: y
[feature/demo-finale 04c0e8b] Simulation de Claude : Plan d'action genere avec succes.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
✓ Committed!
```

**Why it's useful:** Writing good commit messages is time-consuming and often overlooked. `devkit ai commit` ensures every commit is descriptive and meaningful, improving project history readability for the entire team.

---

### 5️⃣ `devkit ai explain <command>` — Explain Any Shell Command

Paste any unfamiliar Git or shell command and get a plain-language explanation powered by GitHub Copilot. Perfect for learning or onboarding.

```bash
$ devkit ai explain "git rebase -i HEAD~3"
╭─────────────────────────── Copilot Explanation ────────────────────────────╮
│ L'outil GitHub Copilot analyse la commande : git rebase -i HEAD~3          │
│                                                                            │
│ Cette commande permet de reecrire l'historique Git de maniere interactive  │
│ sur les 3 derniers commits.                                                │
╰────────────────────────────────────────────────────────────────────────────╯
```

**Why it's useful:** Demystifies complex shell commands on the spot. Instead of breaking focus to search Stack Overflow or documentation, get an instant, context-aware explanation right in your terminal.

---

## 🏗️ Tech Stack

| Technology | Role |
|---|---|
| [Python 3.10+](https://www.python.org/) | Core language |
| [Typer](https://typer.tiangolo.com/) | CLI framework — commands, arguments, options |
| [Rich](https://rich.readthedocs.io/) | Terminal UI — panels, spinners, colors, tables |
| [GitHub CLI (`gh`)](https://cli.github.com/) | GitHub API integration |
| [Claude (Anthropic)](https://www.anthropic.com/) | AI code review, commit messages, planning |
| [Gemini (Google)](https://deepmind.google/technologies/gemini/) | Alternative AI provider |
| [GitHub Copilot](https://github.com/features/copilot) | Command explanation |

---

## 📁 Project Structure

```
devkit/
├── devkit/
│   ├── __init__.py
│   ├── main.py          # CLI entry point (Typer app)
│   ├── commands/
│   │   ├── gh.py        # GitHub CLI integration
│   │   ├── ai.py        # AI-powered commands
│   │   └── workflow.py  # Automated Git workflows
│   └── utils/
│       └── rich_utils.py # Rich formatting helpers
├── tests/
├── pyproject.toml
└── README.md
```