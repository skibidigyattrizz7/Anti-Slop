import ipaddress
import sys
from collections import Counter


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: fixed.py LOGFILE")
    path = sys.argv[1]

    hits_per_ip = Counter()
    skipped = []
    try:
        # errors="replace": one bad byte in a log should not abort the count
        with open(path, encoding="utf-8", errors="replace") as log:
            for number, line in enumerate(log, 1):
                fields = line.split(maxsplit=1)
                first_field = fields[0] if fields else ""
                try:
                    ipaddress.ip_address(first_field)
                except ValueError:
                    skipped.append(number)
                    continue
                hits_per_ip[first_field] += 1
    except OSError as err:
        sys.exit(f"cannot read {path}: {err.strerror}")

    for ip, hits in hits_per_ip.most_common(5):
        print(f"{ip} {hits}")

    if skipped:
        shown = ", ".join(map(str, skipped[:10]))
        print(f"{len(skipped)} lines did not start with an IP (first: {shown})",
              file=sys.stderr)
        sys.exit(1)


main()
