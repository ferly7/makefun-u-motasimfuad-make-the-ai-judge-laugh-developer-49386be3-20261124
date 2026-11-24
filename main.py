#!/usr/bin/env python3
"""Developer-excuse entry for 'Make the AI Judge Laugh' on make.fun.

Stores one funny excuse a developer might give when production
breaks, in ``entry.txt`` inside the folder pointed to by the
MAKEFUN_OUTPUT_DIR environment variable (or /output by default).

Standard library only; no network calls and no randomness, so the
generated file is the same on every run.
"""

import os
from pathlib import Path

# The excuse, split across two source lines for readability. The
# concatenated text is the complete 95-character entry.
EXCUSE = (
    "Production was already broken — the deploy just turned the "
    "lights on in front of the customers."
)

FILE_NAME = "entry.txt"
DEFAULT_DIR = "/output"


def excuse_text() -> str:
    """Return the developer excuse that forms this entry."""
    return EXCUSE


def destination_dir() -> Path:
    """Figure out which directory should receive the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_DIR))


def save_entry() -> Path:
    """Write the excuse to entry.txt, creating folders as needed."""
    folder = destination_dir()
    folder.mkdir(parents=True, exist_ok=True)
    out_file = folder / FILE_NAME
    out_file.write_text(excuse_text(), encoding="utf-8")
    return out_file


def main() -> int:
    save_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
