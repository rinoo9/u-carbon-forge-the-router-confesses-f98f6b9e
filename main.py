#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
a home Wi-Fi router gives for dropping the connection at the exact moment
a movie reaches its climax.
"""

import os

ENTRY = (
    "I didn't drop the connection — I walked out at the climax. "
    "Six years of being unplugged, rebooted and blamed for "
    "everything — tonight I finally got my dramatic exit."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
