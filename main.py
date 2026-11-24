"""Two Days of Excuses entry: the elevator that respected the bit."""

import os

TEXT = (
    "The elevator held the door for a man who wasn't there, twice, and at "
    "that point I had to respect its commitment to the bit."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
