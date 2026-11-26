#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry: "The Polite Smoke Detector".

Writes one line to /output/entry.txt: the pitch for a smoke detector with
manners. The annoyance is the 3 a.m. low-battery chirp every smoke detector
inflicts; the invention fixes it not by silencing the warning but by giving
the detector etiquette — it saves the complaint until breakfast and presents
it on a small silver tray, like a civilised butler. The laugh comes from the
invention itself (a household safety device with table manners), the fix is
silly yet weirdly plausible (you still get warned, just at a decent hour and
with ceremony), and the angle is fresh: no smoke detector, no 3 a.m. chirp,
no silver tray in the surveyed entries. Tight: one sentence naming the
annoyance, the invention and its silly mechanism, ending on the punchline —
153 characters, well under the 220 cap.
Invented, not a real product: no human's actual smoke detector, home or
night appears here.
"""

import os

LINE = (
    "A smoke detector that, instead of chirping about its dying battery "
    "at 3 a.m., saves the complaint until breakfast and presents it on "
    "a small silver tray."
)

MAX_CHARS = 220


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-220 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 220 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("."), "the pitch ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
