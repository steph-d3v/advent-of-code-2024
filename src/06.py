# --- Day 6: Guard Gallivant ---

from sys import argv

def find_guard(grid):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "^":
                return j, i, 0, -1

def is_inside(x, y, grid, cols, rows):
    return 0 <= x < cols and 0 <= y < rows

def is_looping(x, y, dx, dy, grid, cols, rows):
    path = set()
    while True:
        if not is_inside(x, y, grid, cols, rows):
            break
        if grid[y][x] == "#":
            x -= dx
            y -= dy
            dx, dy = -dy, dx  # turn right
            continue
        p = (x, y, dx, dy)
        if p in path:
            return True
        path.add(p)
        x += dx
        y += dy
    return False

with open(argv[1]) as file:
    grid = list(list(c for c in line) for line in file.read().splitlines())

cols, rows = len(grid[0]), len(grid)

x, y, dx, dy = guard = find_guard(grid)

explored = set()

while True:
    explored.add((x, y))
    if not is_inside(nx := x + dx, ny := y + dy, grid, cols, rows):
        break
    if grid[ny][nx] == "#":
        dx, dy = -dy, dx  # turn right
    x += dx
    y += dy

n1, n2 = len(explored), 0

p = None
for x, y in explored:
    if p is not None:
        px, py = p
        grid[py][px] = "."
    grid[y][x] = "#"
    p = x, y
    n2 += is_looping(*guard, grid, cols, rows)

print(n1, n2)