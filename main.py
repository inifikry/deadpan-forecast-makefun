#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes one fixed line (<= 160 chars) to /output/entry.txt.
Fully deterministic: no randomness, no time, no network, no file reads.
"""

import os

FORECAST = (
    "Tonight in Port Anselm, expect a low of 41 and patchy fog that "
    "knows your name. Visibility drops to a quarter mile; "
    "the fog insists it means well."
)


def main() -> None:
    assert 1 <= len(FORECAST) <= 160, "forecast must be 1-160 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
