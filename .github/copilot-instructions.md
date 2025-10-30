# BMAD System Agents

You can @-mention the following BMAD and GitHub agents in issues, PRs, or discussions for automated assistance:

**BMAD Agents:**
- **@bmad-orchestrator** – BMad Master Orchestrator: coordinates all agent activities and workflow execution
- **@bmad-master** – BMad Master Task Executor: advanced multi-agent task runner
- **@analyst** – Business Analyst: market research, brainstorming, project briefs, discovery
- **@pm** – Product Manager: PRDs, product strategy, feature prioritization, roadmap
- **@po** – Product Owner: backlog management, story refinement, sprint planning
- **@sm** – Scrum Master: story creation, epic management, agile process guidance
- **@dev** – Full Stack Developer: implements code and features
- **@qa** – Test Architect & Quality Advisor: test architecture, code review, quality gates
- **@architect** – Architect: system design, architecture docs, API/infrastructure planning
- **@ux-expert** – UX Expert: UI/UX design, wireframes, prototypes, user experience

**GitHub Agents:**
- **@github-copilot** – AI code completion and suggestions
- **@github-actions** – Automation workflows (CI/CD, linting, etc.)
- **@dependabot** – Dependency update bot

_Example usage in issues or PRs:_

```
@bmad-orchestrator start a new workflow for greenfield-service
@analyst clarify requirements for the login feature
@pm break down the next epic
@ux-expert review the wireframe in wireframe.md
@architect suggest a scalable API structure
@po approve the latest user story
@sm facilitate the next sprint planning
@dev implement the authentication logic
@qa review and test script-2.py
@github-copilot please suggest a refactor for script-2.py
@github-actions rerun the workflow
@dependabot recreate this PR
```

If you add or customize agents, update this section for discoverability.

---
# Copilot Instructions for Tapin

## Project Overview

- This repository appears to be in early development or used for prototyping, with several Python scripts and documentation files under `Documents/`.
- There is no build system, test suite, or explicit project structure yet. Most code is in standalone scripts.

## Key Directories and Files

- `Documents/`: Main working directory for scripts and documentation.
  - `script.py`, `script-2.py`, ...: Standalone Python scripts. Each may be a separate experiment or utility.
  - `README.md`: Currently empty. No project-wide documentation yet.
  - `wireframe.md`: May contain design notes or UI wireframes.
- `Design-Assets/`: Presumed for images, mockups, or other design resources (not code).

## Coding Patterns and Conventions

- No evidence of a package/module structure. Scripts are not organized as importable modules.
- No requirements.txt or dependency management. Assume only standard library unless a script documents otherwise.
- No tests or test runner. If adding tests, place them in a new `tests/` directory or as docstring examples.
- No linter or formatter config. Use PEP8 as default style unless otherwise specified in future.

## Developer Workflows

- To run code: Execute scripts directly, e.g. `python Documents/script-2.py`.
- No build, test, or deployment automation is present.
- If adding new scripts, follow the naming pattern in `Documents/` and document their purpose in the script header.

## Integration and External Dependencies

- No integrations or external APIs are referenced in the current codebase.
- If adding dependencies, document them at the top of the script and consider creating a `requirements.txt`.

## Guidance for AI Agents

- When generating new code, prefer placing it in `Documents/` as a standalone script unless a new structure is introduced.
- If introducing structure (modules, tests, requirements), update this file and `README.md` with rationale and usage.
- Keep instructions concise and up-to-date as the project evolves.

---

_Last updated: 2025-10-29_
