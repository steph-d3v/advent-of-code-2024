# --- Day 1: Historian Hysteria ---

from sys import argv

L, R = zip(*(map(int, l.split()) for l in open(argv[1])))
print(sum(abs(l - r) for l, r in zip(sorted(L), sorted(R))), sum(l * R.count(l) for l in L))