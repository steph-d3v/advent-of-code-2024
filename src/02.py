# --- Day 2: Red-Nosed Reports ---

from sys import argv

def is_safe(levels):
    d = [a - b for a, b in zip(levels, levels[1:])]
    return all(1 <= e <= 3 for e in d) or all(-3 <= e <= -1 for e in d)

n1 = n2 = 0

for report in open(argv[1]):
    levels = list(map(int, report.split()))
    n1 += is_safe(levels)
    n2 += any(is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))

print(n1, n2)