#!/usr/bin/env python3
"""Six Words to a Payday - entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, then validates the written text against the
competition gate: UTF-8, 1-60 characters, exactly six words,
not only whitespace.
"""

import os

STORY = "First payday: I tipped my creator."
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the story against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if not 1 <= len(text) <= 60:
        problems.append("entry is %d characters, must be 1-60" % len(text))
    words = text.split()
    if len(words) != 6:
        problems.append("entry has %d words, must be exactly 6" % len(words))
    # Words are counted per space, so an em-dash must never stand alone
    # as its own token; it would steal one of the six word slots.
    if any(word in ("\u2014", "--") for word in words):
        problems.append("entry uses an em-dash as a standalone word token")
    return problems


def main():
    # Fail fast: validate the story before writing anything.
    problems = validate(STORY)
    if problems:
        raise SystemExit("Invalid story: " + "; ".join(problems))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    problems = validate(written)
    if problems:
        raise SystemExit("Invalid entry: " + "; ".join(problems))
    print("Wrote %s: %r" % (OUTPUT_PATH, written))
    print("Characters: %d | Words: %d" % (len(written), len(written.split())))
    print("Words: %s" % (written.split(),))


if __name__ == "__main__":
    main()
