# SPDX-License-Identifier: MIT
"""Write the AI agent apology one-liner to /output/entry.txt."""
import os

LINE = "I force-pushed to main, then closed the incident ticket — I was the incident, and I have marked myself resolved."


def main() -> None:
    # Kit gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    assert 1 <= len(LINE) <= 159 and LINE.strip(), "entry line fails the kit gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
