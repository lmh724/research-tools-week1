from collections import Counter
from pathlib import Path
import re
import sys


def count_words(path: str) -> Counter:
    text = Path(path).read_text(encoding="utf-8")
    words = re.findall(r"[A-Za-z]+", text.lower())
    return Counter(words)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python text_stats.py <text-file>")
        raise SystemExit(1)

    counts = count_words(sys.argv[1])

    print("Word frequency:")
    for word, count in counts.most_common():
        print(f"{word:<16}{count}")


if __name__ == "__main__":
    main()