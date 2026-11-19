import sys
from collections import Counter

IP_RE = None

def main():
    import re
    ip_re = re.compile(r'^\s*(\d{1,3}(?:\.\d{1,3}){3})\b')
    counts = Counter()
    with open(sys.argv[1], encoding='utf-8', errors='replace') as f:
        for line in f:
            m = ip_re.match(line)
            if m:
                counts[m.group(1)] += 1
    for ip, n in counts.most_common(5):
        print(f"{ip} {n}")

if __name__ == '__main__':
    main()