"""Entry for The Most Honest Outage Line: writes the status line to /output/entry.txt."""

import os

TEXT = "We're down. Nobody knows why. We've restarted it twice, blamed the intern once, and are now refreshing this page exactly as often as you are."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
