#!/usr/bin/env python3
"""Print each student's average score, lowest average first.

Usage: python3 t-b.py [grades.csv]
"""
import csv
import sys
from collections import defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "grades.csv"
scores = defaultdict(list)

with open(path, newline="") as f:
    for line_no, row in enumerate(csv.DictReader(f), start=2):
        try:
            scores[row["student"]].append(float(row["score"]))
        except (KeyError, TypeError, ValueError) as exc:
            # Stop on the first bad row: an average over a silently skipped score is wrong.
            sys.exit(f"{path} line {line_no}: cannot read {row!r} ({exc})")

averages = {name: sum(vals) / len(vals) for name, vals in scores.items()}
for name in sorted(averages, key=lambda student: (averages[student], student)):
    print(f"{name}: {averages[name]:.2f}")
