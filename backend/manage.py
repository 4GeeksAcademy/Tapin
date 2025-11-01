#!/usr/bin/env python3
"""Simple management wrapper for common backend maintenance tasks.

Primarily provides a small wrapper to run Alembic migrations from a virtualenv.
"""
import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ALEMBIC_INI = REPO_ROOT / "alembic.ini"


def alembic_upgrade_head():
    """Run `alembic -c alembic.ini upgrade head` using the current Python environment."""
    cmd = [sys.executable, "-m", "alembic", "-c", str(ALEMBIC_INI), "upgrade", "head"]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=str(REPO_ROOT))


def main():
    if len(sys.argv) < 2:
        print("Usage: manage.py <command>\n\nCommands:\n  upgrade   Run alembic upgrade head")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd in ("upgrade", "migrate", "migrations"):
        alembic_upgrade_head()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(2)


if __name__ == "__main__":
    main()
