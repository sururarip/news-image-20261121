"""Entry program for make.fun news-image-20261121.

Writes the bundled front-page image to the output directory. The
grader runs this with no network, so the image ships inside the repo
and this program only copies it. Deterministic: the same bytes are
written on every run. The output directory comes from
MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png missing from the repository")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
