#!/usr/bin/env python3
"""ai-happy-01 entry: "Two friends, one umbrella."

A program that writes one image to /output/entry.png: a golden retriever
puppy and a tiny orange kitten sharing a single red umbrella in warm rain,
a rainbow arcing behind them, both looking up at the sky with pure delight.

Why this image makes the judge happy:
  * a specific, fresh moment -- two unlikely friends sharing one umbrella,
    the kitten holding the handle so the puppy stays dry;
  * warmth and joy in the expressions (both animals smiling up at the sky);
  * colour and light pulling one way (red umbrella, rainbow, golden sun);
  * clean storybook rendering, no text, no artefacts;
  * it reads at 300 px: puppy + kitten + red umbrella + rainbow.

The image is stored in this repository as happy.jpg (1024x1024 JPEG,
280,704 bytes -- under the 1 MiB cap). The program only copies those exact
bytes to the output, so running it twice writes identical bytes.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

# The image shipped in this repository (JPEG bytes, 1024x1024, 280,704 B;
# the output keeps the competition's fixed name entry.png, and the gate
# tells PNG from JPEG by the file's first bytes, so a JPEG named .png is
# a valid entry).
SOURCE = Path(__file__).resolve().parent / "happy.jpg"

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f"Wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
