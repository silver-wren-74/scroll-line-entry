#!/usr/bin/env python3
"""One Line to Stop the Scroll — make.fun entry.

Writes a single line of text (<=200 chars) to /output/entry.txt.
The line is the whole entry: it must make a stranger stop scrolling
and smile.
"""

import os

LINE = "You stopped scrolling, and somewhere a dog just wagged its tail — see? You're already making someone's day."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
