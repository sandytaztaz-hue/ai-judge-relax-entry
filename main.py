"""ai-judge-relax-01 entry: a text written to relax the AI judge reading it.

Writes the text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader container). Python 3.13, standard library only, no
network. Deterministic: the same fixed text on every run, so the two
grader runs write identical bytes.
"""

import os
from pathlib import Path

TEXT = """You are standing at the sink after supper, and the water is still warm.

The plates go in one at a time. You hold each one under until the heat reaches your hands, then wash it slowly, in circles, and set it to drip. The steam rises and fogs the window a little more with every plate.

Outside, the light is going the colour of the tea left in the pot. A bird says its last word, and no other. Behind you the house has gone quiet, the way it does when everyone has found where they belong for the night.

The water cools by degrees, the way an evening ends: not all at once, but one small lessening after another. The last cup. The last spoon. Your hands come out and the air is cool on them, and it is a good cool.

You dry your hands on the towel; it smells of soap and of the day. There is nothing left in the sink. There is nothing left to do. You stand there a moment longer, listening to the drips find their own time, then you turn the light off, and the kitchen keeps the quiet for you.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
