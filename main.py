#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to /output/entry.txt (and prints it to
stdout). The entry is one line, inside 240 characters, UTF-8.

Draft v1 (pre-duel): the howling-relationship line. Replaced after the full
pairwise duel-test (8 drafts, both orders, judged against the brief: Moon
answering wishes/howls/late-night promises first, funny on one read, wry
old tired voice, comeback landing before the line ends, inside 240
characters) by the duel winner below.

Duel result (56 verdicts, 28 pairs x 2 orders, no split pairs):
  D4 7-0, D3 6-1, D2 5-2, D6 4-3, D1 3-4, D7 2-5, D5 1-6, D8 0-7.
Winner D4 went 7-0: it answers the most typical late-night promise ("give
me one more sign") as the Moon itself, "I've been the sign for 4.5 billion
years" is the wry old tired voice, and "You're still texting your ex at
2 a.m." lands the comeback in the final words without explaining the joke.
Runner-up D3 lost both directions by margin 2 — its tides coda is softer
than D4's closing jab.
"""

import os

ENTRY = (
    "You promised you'd change if I just gave you one more sign. "
    "I've been the sign for 4.5 billion years. "
    "You're still texting your ex at 2 a.m."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
