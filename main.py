#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Rain, a leaf on a river, stars keeping their old
distances, and a night wide enough to hold the reader exactly as they are.
"""

import os

TEXT = (
    "Rain on a tin roof, one drop, then another, and nobody counting. "
    "A leaf rides the river down, slow as a thought you never have to finish. "
    "The stars keep their old distances, and the night is wide \u2014 "
    "it has always been \u2014 and it holds you exactly as you are."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
