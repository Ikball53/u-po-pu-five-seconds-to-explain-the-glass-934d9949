"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat offers in its own defence
in the five seconds after sweeping a glass off the table.
"""

import os

LINE = "It was sitting in my sunbeam, so I relocated it to the floor."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
