"""Print the 20 most frequent words in a text file."""

from collections import Counter
from pathlib import Path
import re
import sys


WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {Path(sys.argv[0]).name} <input_file>", file=sys.stderr)
        raise SystemExit(2)

    input_path = Path(sys.argv[1])
    try:
        text = input_path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Cannot read {input_path}: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    counts = Counter(word.lower() for word in WORD_PATTERN.findall(text))
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:20]:
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
