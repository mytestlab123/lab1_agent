#!/usr/bin/env python3
"""Build the minimal direct-code ZIP for Experiment 01."""

from pathlib import Path
import shutil
import zipfile

HERE = Path(__file__).resolve()
EXPERIMENT = HERE.parents[1]
APP = EXPERIMENT / "app" / "main.py"
OUT_DIR = EXPERIMENT.parents[1] / ".build" / "agentcore-runtime"
OUT = OUT_DIR / "deployment_package.zip"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(APP, "main.py")

    print(OUT)


if __name__ == "__main__":
    main()
