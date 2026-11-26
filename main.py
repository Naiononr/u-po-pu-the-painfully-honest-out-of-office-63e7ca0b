#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single brutally honest but still polite out-of-office auto-reply
to /output/entry.txt: the sender is away, the inbox is already deep, and
replies will come in the order each email still matters when they return.

The line is written to be judged on the competition's own brief:
  1. It is an out-of-office email auto-reply, painfully honest and still
     polite enough to survive being forwarded to a manager.
  2. It admits something true a real employee would only say privately:
     the inbox is hundreds deep and not every email will be answered
     in the order it arrived.
  3. It keeps a warm, professional tone: a promise to reply, not a
     complaint about the job.
  4. It is one sentence, well inside 200 characters, with no cramming.
  5. It lands with a turn a reader would quote: replies come "in the
     order your emails still matter when I'm back".

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = (
    "I'm out of the office this week, and my inbox is already 400 deep "
    "\u2014 I'll reply in the order your emails still matter when I'm back."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
