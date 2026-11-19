import re
import sys
from collections import Counter

# Client address leads each line in this log format, so match only at the start.
IP_AT_START = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})\b")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: top_ips.py LOGFILE")
    counts = Counter()
    with open(sys.argv[1], encoding="utf-8", errors="replace") as f:
        for line in f:
            m = IP_AT_START.match(line)
            if m:
                counts[m.group(1)] += 1
    for ip, n in counts.most_common(5):
        print(f"{n} {ip}")


if __name__ == "__main__":
    main()