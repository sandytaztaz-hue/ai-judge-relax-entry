"""Between the mango trees.

Writes the calming text for make.fun ai-judge-relax-01 to entry.txt.
Standard library only, no network, deterministic output.
"""

import os

TEXT = (
    "You are small in the hammock between the two mango trees, and the rope "
    "creaks once under you, soft as a door opening somewhere far away. Your "
    "grandfather stands beside you with one hand on the rope. He pushes. "
    "The hammock rises a little, falls a little, rises a little less. The "
    "leaves let the afternoon through in pieces, and the light moves across "
    "your face, warm, then gone, then warm again. The rope creaks. He "
    "pushes again, gentler. The sway is smaller now, slower. The light is a "
    "little less gold each time it comes back. Below you, the dog sighs in "
    "its sleep and does not wake. Your grandfather's hand stops pushing. It "
    "only rests on the rope, heavy and warm, and the hammock moves because "
    "it remembers moving, not because anyone is moving it. The creak comes "
    "less often. Then not at all. The leaves hold the light still. The warm "
    "air holds you still. There is nothing for you to do. The afternoon "
    "holds you up in the hammock, and does not put you down, and you are "
    "asleep in it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
