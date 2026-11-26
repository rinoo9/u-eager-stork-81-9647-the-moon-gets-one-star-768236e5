#!/usr/bin/env python3
"""The Moon Gets One Star.

A one-star review of the Moon, written as a single line of at most
120 characters. The program writes that review deterministically to
/output/entry.txt (and prints it), so every run produces the same bytes.
"""

import os

REVIEW = (
    "One star. Late every night, gone a whole week each month, "
    "yet still takes full credit for the tides. Unreliable."
)


def main() -> None:
    # The gate only judges texts of 1 to 120 characters; never ship a longer line.
    assert 1 <= len(REVIEW) <= 120, f"review is {len(REVIEW)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
