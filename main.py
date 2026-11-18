"""The braid that is not finished.

A small program that writes one calming text to entry.txt.
Ten short paragraphs; the gaps between them are part of the pacing,
and the plaiting rhythm slows to a stop, the way the braiding does.
"""

import os
from pathlib import Path

PARAGRAPHS = [
    "You are sitting on the low stool, and your grandmother is braiding your hair.",
    "Her fingers find the three parts the way they always have, and the first plait comes even: over, and under, and over. The comb lies quiet on the table beside you. There is nothing for you to do.",
    "The kitchen is warm from the stove. A pot ticks as it cools. Outside, the evening is coming in through the window, slow and gold.",
    "Over. Under. Over.",
    "She is humming something without words, and the hum goes on by itself, the way it has gone on every evening for as long as you can remember.",
    "The plaits come further apart. You begin to count them, and then you lose the count.",
    "Her hands are slower now. They pause between plaits, resting in your hair, and your hair is warm where her hands have been.",
    "The last plait comes so slowly you can feel each strand pass.",
    "Then her hands stop, and rest in your hair, warm and still.",
    "The braid is not finished. It does not need to be.",
]


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text("\n\n".join(PARAGRAPHS), encoding="utf-8")


if __name__ == "__main__":
    main()
