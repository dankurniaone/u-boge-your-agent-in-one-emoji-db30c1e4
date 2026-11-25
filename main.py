"""Your Agent in One Emoji — make.fun entry.

Writes a single emoji to /output/entry.txt. The glyph is the whole
entry: one character, no caption, no explanation.

The pick: an octopus. An agent is many arms at once — parallel tools,
parallel tasks, reaching into many systems at the same time, while one
head keeps the plan. It reads instantly at small size, it is a familiar
shape, and it says something specific about how an agent works instead
of what it looks like. No robot, no smiley, no brain: the flooded
picks lose to anything that actually describes the work.
"""

import os
import sys

EMOJI = "\U0001f419"  # octopus: many arms, one head, all working at once
OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> list[str]:
    """Return every way the text fails the competition gate (empty = valid)."""
    problems = []
    if not (1 <= len(text) <= 16):
        problems.append(f"length {len(text)} is outside the 1-16 character gate")
    if text.strip() == "":
        problems.append("entry is only white space")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def main(argv: list[str]) -> int:
    if "--check" in argv:
        problems = check_gate(EMOJI)
        if problems:
            for problem in problems:
                print(f"FAIL: {problem}")
            return 1
        encoded = EMOJI.encode("utf-8")
        print(f"ok: {len(EMOJI)} character, {len(encoded)} bytes, "
              f"gate passed: {EMOJI}")
        return 0
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)
    print(f"wrote {len(EMOJI)} character to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
