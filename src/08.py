# --- Day 8: Resonant Collinearity ---

from collections import defaultdict
from itertools import combinations
from sys import argv

def get_antennas(grid):
    antennas = defaultdict(set)
    for location, c in grid.items():
        if c != ".":
            antennas[c].add(location)
    return antennas

def get_antinodes(a1, a2, grid, r):
    x1, y1 = a1
    x2, y2 = a2
    dx, dy = x2 - x1, y2 - y1
    n1 = x1 + r * dx, y1 + r * dy
    n2 = x2 - r * dx, y2 - r * dy
    return set((x, y) for x, y in (n1, n2) if (x, y) in grid)

with open(argv[1]) as file:
    lines = file.read().splitlines()

grid = {(i, j): c for j, line in enumerate(lines) for i, c in enumerate(line)}
antennas = get_antennas(grid)

s1, s2 = set(), set()
for _, locations in antennas.items():
    for a1, a2 in combinations(locations, 2):
        r, s = 0, set()  # r: radius around antenna
        while s != (sr := s.union(a := get_antinodes(a1, a2, grid, r := r + 1))):
            if r == 2:
                s1 = s1.union(a)
            s2 = s2.union(s := sr)
        s2 = s2.union(s1)

print(len(s1), len(s2))