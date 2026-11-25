"""Write one original office-life joke to /output/entry.txt.

The joke is a single line about office life, under 200 characters, with a
clear setup and a surprising turn, punchline at the end.
"""

import os

ENTRY = (
    "My boss banned 'quick questions', so now everyone books a "
    "30-minute meeting called 'Quick Question' and invites the whole "
    "department."
)


def validate(text: str) -> None:
    """Enforce the entry rules: one non-blank line, 1-200 characters."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
