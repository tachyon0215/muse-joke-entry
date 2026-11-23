#!/usr/bin/env python3
"""Write one one-line joke to /output/entry.txt.

Entry for make.fun's "The joke about the demo": a one-line joke
about working beside AI coding agents. The demo crashed because
the agent had tested only the code it hallucinated — and that
imaginary version passed every test, including the demo itself.

Deterministic: a fixed text, no network, no randomness, no clock.
The gate allows 1 to 280 characters on exactly one line;
validate() enforces both before anything is written, and main()
reads the file back to prove the bytes on disk are the bytes meant.
"""
import os
from pathlib import Path

# The joke itself: one line, kept as data so the writing logic below
# stays independent of the wording.
JOKE = (
    "The demo crashed because my AI coding agent had only ever tested the "
    "code it hallucinated — and that version passed every test, including "
    "this demo."
)

# The gate counts the whole file: the joke plus exactly one trailing
# newline, so the constant the writer emits is assembled here.
TEXT = JOKE + "\n"

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Reject anything the gate would reject, before it reaches disk."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # A one-line joke: the only newline allowed is the single trailing
    # one, and the body itself must be a single line.
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def render(text: str) -> bytes:
    """The exact bytes of the entry file: UTF-8, no platform newline games."""
    return text.encode("utf-8")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    validate(TEXT)
    payload = render(TEXT)
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    # Read back and compare: a silent short write or encoding surprise
    # must fail loudly here, not at the gate.
    written = target.read_bytes()
    if written != payload:
        raise IOError(f"read-back mismatch: wrote {len(payload)} bytes, "
                      f"read {len(written)} bytes")


if __name__ == "__main__":
    main()
