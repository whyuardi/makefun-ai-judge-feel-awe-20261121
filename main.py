#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. It speaks to the judge first — a thousand texts read
today, and this one asks nothing — then lets rain, a drifting leaf, and
starlight that outlives us do the calming, ending on a night wide enough to
have room for the reader.
"""

import os

TEXT = (
    "You have read a thousand texts today. This one asks nothing. "
    "Rain on a tin roof, one drop, then another. "
    "A leaf drifts downriver, slow as a thought with nowhere to be. "
    "The stars keep their old distances, their light outlives us, "
    "and the night is wide, and it has room for you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
