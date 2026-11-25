"""Copy the pre-rendered entry image to the output directory.

The entry image (entry.png, 1024x1024, drawn during the build session) sits
next to this file in the repository. This program only copies it to
$MAKEFUN_OUTPUT_DIR/entry.png and verifies the copy byte-for-byte with
SHA-256, failing hard on any mismatch. Standard library only, no network.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1048576
MAX_DIMENSION = 1024


def check_png_gate(path):
    """Enforce the competition gate: PNG, at most 1024x1024, at most 1 MiB."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return "not a PNG file"
    if header[12:16] != b"IHDR":
        return "PNG has no IHDR chunk"
    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        return "image is %dx%d, over the 1024x1024 limit" % (width, height)
    if path.stat().st_size > MAX_BYTES:
        return "image is over the 1 MiB limit"
    return None


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    target_dir = Path(out_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    source_size = source.stat().st_size
    target_size = target.stat().st_size
    if source_size != target_size:
        print("size mismatch: source %d bytes, copy %d bytes"
              % (source_size, target_size), file=sys.stderr)
        return 1
    if sha256_of(source) != sha256_of(target):
        print("sha256 mismatch between source and copy", file=sys.stderr)
        return 1
    gate_error = check_png_gate(target)
    if gate_error:
        print("gate check failed: %s" % gate_error, file=sys.stderr)
        return 1
    print("entry.png copied and verified: %d bytes, sha256 %s"
          % (target_size, sha256_of(target)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
