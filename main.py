"""Entry program for make.fun news-image-20261121.

Writes the bundled front-page image to the output directory. The
grader runs this with no network, so the image ships inside the repo
and this program only copies it. Deterministic: the same bytes are
written on every run. The image's SHA-256 is checked before copying,
so a corrupted or wrong file is never submitted silently. The output
directory comes from MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
EXPECTED_SHA256 = "1121e44de6b938108ba2aacded843d6265bf38f8ed14a2c9b12b248cf816acfa"


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png missing from the repository")
    digest = hashlib.sha256()
    with open(SOURCE, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    if digest.hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.png failed integrity check: hash mismatch")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
