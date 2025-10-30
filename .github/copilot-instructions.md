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
