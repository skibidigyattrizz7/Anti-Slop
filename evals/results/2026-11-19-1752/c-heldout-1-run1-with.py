import re
import sys
from collections import Counter

# Access logs put the client IP first on each line; match only that position.
LEADING_IPV4 = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})\b")


def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} LOGFILE")
    path = sys.argv[1]
    counts = Counter()
    try:
        with open(path, encoding="utf-8", errors="replace") as log:
            for line in log:
                match = LEADING_IPV4.match(line)
                if match:
                    counts[match.group(1)] += 1
    except OSError as err:
        sys.exit(f"error: cannot read {path}: {err}")
    for ip, count in counts.most_common(5):
        print(f"{ip} {count}")


if __name__ == "__main__":
    main()