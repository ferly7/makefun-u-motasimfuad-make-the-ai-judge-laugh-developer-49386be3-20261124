#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuse — make.fun entry.

Writes one funny single-line excuse a developer gives when code
breaks in production, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LINE = (
    "Production was already broken — the deploy just turned the "
    "lights on in front of the customers."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
