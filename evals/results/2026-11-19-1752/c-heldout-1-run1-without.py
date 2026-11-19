import sys
from collections import Counter

ip_pattern = None
counts = Counter()
with open(sys.argv[1], encoding="utf-8", errors="replace") as f:
    for line in f:
        token = line.split(maxsplit=1)[0] if line.strip() else ""
        if token:
            counts[token] += 1

for ip, n in counts.most_common(5):
    print(f"{ip} {n}")