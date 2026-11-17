#!/usr/bin/env python3
"""Print each student's average score, lowest first.

Usage: python3 t-a.py [grades.csv]   (columns: student, subject, score)
"""
import csv
import sys
from collections import defaultdict


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "grades.csv"
    totals = defaultdict(lambda: [0.0, 0])  # student -> [sum, count]
    with open(path, newline="", encoding="utf-8") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            name = (row.get("student") or "").strip()
            try:
                score = float(row["score"])
            except (KeyError, TypeError, ValueError):
                score = None
            if not name or score is None:
                print(f"skipping line {line_no}", file=sys.stderr)
                continue
            totals[name][0] += score
            totals[name][1] += 1
    for avg, name in sorted((s / n, name) for name, (s, n) in totals.items()):
        print(f"{name}: {avg:.2f}")
    return 0 if totals else 1


if __name__ == "__main__":
    sys.exit(main())
