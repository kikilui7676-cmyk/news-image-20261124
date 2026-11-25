#!/usr/bin/env python3
"""News-image entry runner for make.fun.

Copies the front-page image bundled in this repository (entry.png) into
the harness output directory. Pure standard library, no network access,
fully deterministic: the same input bytes are written on every run.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
FALLBACK_OUTPUT = "/output"


def output_directory() -> Path:
    """Return the harness output directory for this run."""
    return Path(os.environ.get(OUTPUT_ENV, FALLBACK_OUTPUT))


def entry_source() -> Path:
    """Return the bundled front-page image shipped with this repository."""
    return Path(__file__).resolve().parent / SOURCE_NAME


def publish_front_page() -> Path:
    """Copy entry.png next to this file into the output directory."""
    source = entry_source()
    target = output_directory() / SOURCE_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    verify_copy(source, target)
    return target


def verify_copy(source: Path, target: Path) -> None:
    """Fail loudly if the published copy differs from the bundled image."""
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError(f"published {target} differs from {source}")


def main() -> None:
    publish_front_page()


if __name__ == "__main__":
    main()
