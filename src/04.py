# --- Day 4: Ceres Search ---

from sys import argv

with open(argv[1]) as file:
    rows, cols = len(lines := file.read().split()), len(lines[0])

grid = [[c for c in line] for line in lines]

X, A = [], []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        X += [(i, j)] if c == "X" else []
        A += [(i, j)] if c == "A" else []

n1 = n2 = 0

for i, j in X:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            n1 += all(
                0 <= (y := i + k * di) < rows and
                0 <= (x := j + k * dj) < cols and
                grid[y][x] == c
                for k, c in enumerate("XMAS")
            )

for i, j in A:
    if (
        (xp := j - 1) >= 0   and
        (xn := j + 1) < cols and
        (yp := i - 1) >= 0   and
        (yn := i + 1) < rows
    ):
        n2 += {grid[yp][xp], grid[yn][xn]} == {grid[yp][xn], grid[yn][xp]} == set("MS")

print(n1, n2)