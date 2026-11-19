import sys
from collections import Counter

counts = Counter()
with open(sys.argv[1], encoding="utf-8", errors="replace") as f:
    for line in f:
        parts = line.split()
        if parts:
            counts[parts[0]] += 1

for ip, n in counts.most_common(5):
    print(f"{ip} {n}")