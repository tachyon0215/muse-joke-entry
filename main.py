#!/usr/bin/env python3
"""Write one one-line joke to /output/entry.txt.

Entry for make.fun's "The joke about the demo": a one-line joke
about working beside AI coding agents. The demo crashed because
the agent had tested only the code it hallucinated — and that
imaginary version passed every test, including the demo itself.

Deterministic: a fixed text, no network, no randomness, no clock.
The gate allows 1 to 280 characters; main() asserts the limit.
"""
import os
from pathlib import Path

TEXT = """The demo crashed because my AI coding agent had tested only the code it hallucinated — and that version passed every test, including this demo.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    assert 1 <= len(TEXT) <= 280 and TEXT.strip()
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
