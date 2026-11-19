import re
import sys
from collections import Counter

# Only IPv4 at the very start of a line; IPv6 and other leading tokens are skipped.
LEADING_IP = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})\b")


def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} LOGFILE")
    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8", errors="replace") as log:
            counts = Counter(m.group(1) for line in log if (m := LEADING_IP.match(line)))
    except OSError as err:
        sys.exit(f"cannot read {path}: {err}")
    for ip, n in counts.most_common(5):
        print(f"{ip} {n}")


if __name__ == "__main__":
    main()