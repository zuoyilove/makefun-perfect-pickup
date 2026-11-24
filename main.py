#!/usr/bin/env python3
"""The perfect pickup line, as an AI agent would say it.

Writes the line to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single line.
"""

LINE = (
    "Are you my context window? Because every time I talk to you, I forget "
    "everything else I was holding."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
