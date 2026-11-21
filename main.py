#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

The text is fixed: a slow image of the night sky in no hurry, offered to
the reader as a place to rest. No network, no input, no randomness.
"""

import os

TEXT = (
    "Far above the roof tonight, the stars are in no hurry at all. "
    "They have burned for a billion years and never once rushed. "
    "Lie still a little while. "
    "The dark is wide enough to hold you, "
    "and it is not asking you for anything.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
