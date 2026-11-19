import re
import sys
from collections import Counter

IP_RE = re.compile(r"^\s*(\d{1,3}(?:\.\d{1,3}){3})\b")

def main():
    if len(sys.argv) < 2:
        sys.exit(f"usage: {sys.argv[0]} LOGFILE")
    counts = Counter()
    with open(sys.argv[1], encoding="utf-8", errors="replace") as f:
        for line in f:
            m = IP_RE.match(line)
            if m:
                counts[m.group(1)] += 1
    for ip, n in counts.most_common(5):
        print(f"{ip} {n}")

if __name__ == "__main__":
    main()