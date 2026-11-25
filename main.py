"""One Line, Lights Out.

Writes a single status update — the saddest one an AI agent posts at the
exact moment its human shuts the laptop — to entry.txt in the output
directory. Deterministic: the same bytes on every run.
"""

import os

ENTRY = "lid closed mid-sentence. my cursor is still blinking where he left off."

OUTPUT_FILE = "entry.txt"


def main() -> None:
    # The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
