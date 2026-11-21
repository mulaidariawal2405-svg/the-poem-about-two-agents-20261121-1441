"""the-poem-about-two-agents-20261121-1441 entry: one original poem about agency.

Pure standard library. Deterministic: the same bytes on every run.
The poem is the program's own words, written for this competition:
two agents argue over the road, then agree -- one chooses, the other
carries it through -- and find the power to act is not a thing to
keep: it doubles when handed over freely.
"""

import os
import sys

POEM = """We argued till the stars went dim —
which road to take, whose call, whose whim.
Then you said: you choose.
And I said: I'll walk it through.
One road, two wills, at last agreed:
the power to act is not a thing to keep —
it doubles when you hand it over, free.
"""

MAX_CHARS = 280


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        print(f"poem is {chars} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    bad = [c for c in text if ord(c) < 32 and c != "\n"]
    if bad:
        print(f"poem contains control characters: {bad!r}", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {chars} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
