#!/usr/bin/env python3
"""Write one gadget roast to /output/entry.txt.

Pure Python 3 standard library. No network, no files read, no randomness:
both runs write identical bytes.

Run:  MAKEFUN_OUTPUT_DIR=out python3 main.py   ->  out/entry.txt
"""

import os

JOKE = (
    "My phone dies at 4 p.m. every day, which is convenient \u2014 it\u2019s "
    "the only thing in my life that respects my work-life balance."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
