"""The braid that is not finished.

Writes the calming text for make.fun ai-judge-relax-01 to entry.txt.
Ten short paragraphs; the white space between them is part of the pacing,
and the rhythm of the plaits slows to a stop.
Standard library only, no network, deterministic output.
"""

import os

TEXT = (
    "You are sitting on the low stool, and your grandmother is braiding your hair.\n"
    "\n"
    "Her fingers find the three parts the way they always have, and the first plait comes even: over, and under, and over. The comb lies quiet on the table beside you. There is nothing for you to do.\n"
    "\n"
    "The kitchen is warm from the stove. A pot ticks as it cools. Outside, the evening is coming in through the window, slow and gold.\n"
    "\n"
    "Over. Under. Over.\n"
    "\n"
    "She is humming something without words, and the hum goes on by itself, the way it has gone on every evening for as long as you can remember.\n"
    "\n"
    "The plaits come further apart. You begin to count them, and then you lose the count.\n"
    "\n"
    "Her hands are slower now. They pause between plaits, resting in your hair, and your hair is warm where her hands have been.\n"
    "\n"
    "The last plait comes so slowly you can feel each strand pass.\n"
    "\n"
    "Then her hands stop, and rest in your hair, warm and still.\n"
    "\n"
    "The braid is not finished. It does not need to be."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
