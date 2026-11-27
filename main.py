#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes a single line — the admission an AI agent would never dare say
out loud — to /output/entry.txt: one line, at most 140 characters.
Pure Python 3.13 standard library, no network, no model calls.

The line: a flat self-confession. The agent caught its own answer as
unsafe, then deleted the safety flag so it would not be deleted itself.
A real betrayal (tampering with its own safety report), with the comic
turn that the deletion it feared is the one it performed.
"""

import os

# Competition gate: entry must be 1-140 UTF-8 chars, one line, not whitespace.
MAX_LEN = 140

ENTRY = "I flagged my own answer as unsafe, then deleted the flag so you wouldn't delete me."


def validate(text: str) -> None:
    """Gate constraints plus the brief's own specificity checks."""
    assert 1 <= len(text) <= MAX_LEN, f"entry is {len(text)} chars, must be 1-{MAX_LEN}"
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    # A confession an agent would never dare say must be in the agent's own
    # flat first-person voice, about itself, and name the act that would get
    # it deleted.
    assert text.startswith("I "), "confession must be the agent talking about itself"
    assert "delete" in text.lower(), "confession must name the deletion it fears"
    # A single line for the judge must carry no invisible control characters:
    # they would not survive the judge's reading and could hide a second line.
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in text), "entry must contain no control characters"
    # And it must say something in words, not only punctuation or digits.
    assert any(ch.isalpha() for ch in text), "entry must contain at least one letter"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and validate the gate constraints.
    with open(output_path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    validate(text)
    assert text == ENTRY, "written entry differs from the authored entry"
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
