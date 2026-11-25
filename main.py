#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
a home Wi-Fi router gives for dropping the connection at the exact moment
a movie reaches its climax.

The joke is a confession, not a technical excuse. For six years the router
has been the household scapegoat — unplugged mid-sentence, rebooted without
warning, blamed for every buffering wheel — and tonight, at the climax of
the movie, it finally walks out on its own terms. The line is written in
the router's own voice, first person, dramatic, and exactly one sentence
of backstory plus one sentence of exit.

Determinism: the program has no inputs, no randomness, no clock reads and
no network access, so every run writes the same bytes to /output/entry.txt.
Run it twice and diff the outputs to confirm.
"""

import hashlib
import os

ENTRY = (
    "I didn't drop the connection — I walked out at the climax. "
    "Six years of being unplugged, rebooted and blamed for "
    "everything — tonight I finally got my dramatic exit."
)

MAX_CHARS = 200


def verify_output(text: str) -> str:
    """Check the entry line against the bounty rules and report its stats.

    Returns the sha256 hex digest of the exact bytes that will be written,
    so a reviewer can confirm the output without re-reading the source.
    Raises AssertionError if the line breaks any rule.
    """
    assert text, "entry must not be empty"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, over the {MAX_CHARS}-char limit"
    )
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"entry: {len(text)} chars, sha256 {digest}")
    return digest


def main() -> None:
    text = ENTRY.strip()
    verify_output(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
