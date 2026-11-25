#!/usr/bin/env python3
"""Publish the bundled front-page image for the news-image-20261124 entry.

The entry is a single PNG: one newspaper front page summing up the world's
news of Tuesday 24 November 2026. This script does the only thing an
entrypoint needs to do -- copy that bundled image into the output directory
the harness names, so the published artifact is exactly the image in the
repository.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

BUNDLED_IMAGE = "entry.png"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_copy(source: Path, target: Path) -> None:
    """Fail loudly if the published copy differs from the bundled image."""
    if sha256_of(source) != sha256_of(target):
        raise SystemExit(
            f"verification failed: {target} differs from {source}"
        )


def bundled_image_path() -> Path:
    """Return the path of the image shipped next to this script."""
    return Path(__file__).resolve().parent / BUNDLED_IMAGE


def publish(source: Path, destination_dir: Path) -> Path:
    """Copy the bundled image into destination_dir and return its new path."""
    destination_dir.mkdir(parents=True, exist_ok=True)
    target = destination_dir / source.name
    shutil.copyfile(source, target)
    return target


def main() -> int:
    source = bundled_image_path()
    if not source.is_file():
        print(f"bundled image missing: {source}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = publish(source, out_dir)
    verify_copy(source, target)
    print(f"published {target} (sha256 {sha256_of(target)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
