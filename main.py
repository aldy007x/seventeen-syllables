"""Seventeen Syllables of Debugging entry for make.fun.

Writes one haiku about debugging to /output/entry.txt, where the house
judge reads it. The haiku is three lines in the 5-7-5 syllable shape,
at most 200 characters in total.
"""

import os

HAIKU = """One more print statement
and the bug moves somewhere else
it knows I'm watching"""

# Syllable counts for every word in the haiku, counted by hand.
SYLLABLES = {
    "one": 1,
    "more": 1,
    "print": 1,
    "statement": 2,
    "and": 1,
    "the": 1,
    "bug": 1,
    "moves": 1,
    "somewhere": 2,
    "else": 1,
    "it": 1,
    "knows": 1,
    "i'm": 1,
    "watching": 2,
}

EXPECTED = (5, 7, 5)


def count_line(line: str) -> int:
    """Count the syllables of one line using the explicit map above."""
    total = 0
    for word in line.lower().replace(",", "").split():
        if word not in SYLLABLES:
            raise ValueError(f"no syllable count for word: {word!r}")
        total += SYLLABLES[word]
    return total


def validate(haiku: str) -> None:
    """Enforce the bounty gate: 3 lines, 5-7-5, 1-200 chars, not blank."""
    if not haiku.strip():
        raise ValueError("haiku must not be blank")
    if len(haiku) > 200:
        raise ValueError(f"haiku is {len(haiku)} chars, over the 200 limit")
    lines = haiku.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, got {len(lines)}")
    for line, expected in zip(lines, EXPECTED):
        if not line.strip():
            raise ValueError("haiku lines must not be blank")
        got = count_line(line)
        if got != expected:
            raise ValueError(
                f"line {line!r} has {got} syllables, expected {expected}"
            )


def main() -> None:
    validate(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read it back: the file on disk must be byte-for-byte the haiku.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != HAIKU:
        raise ValueError("written entry does not match the haiku")
    print(HAIKU)


if __name__ == "__main__":
    main()
