#!/usr/bin/env python3
"""Make.fun entry: The One-Liner Groan-Off.

Writes a single original one-line dad joke to /output/entry.txt.
Python 3.13, standard library only. Deterministic: no randomness,
no network, no environment reads, no input files.
"""

import os

JOKE = (
    "I asked the dryer where my third left sock went this week, "
    "and it said the case is still spinning."
)

MAX_CHARS = 140


def main() -> None:
    line = JOKE.strip()
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if "  " in line:
        raise SystemExit("entry has a double space")
    if not line.endswith("."):
        raise SystemExit("entry must end on its punchline with a full stop")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print(f"Wrote {len(line)}-char entry to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
