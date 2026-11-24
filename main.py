#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt (120 characters or fewer, UTF-8 text).
"""

import os

LINE = "Out of office: I'm a fern, unwatered since March. I've unionized with the cactus \u2014 your email is now compost."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line must be 1-120 chars, got {len(text)}"
    # MAKEFUN_OUTPUT_DIR overrides the output directory for local checks;
    # the grader runs with the default /output and gets identical bytes.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
