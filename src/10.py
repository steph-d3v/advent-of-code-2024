# --- Day 10: Hoof It ---

from sys import argv

def explore(grid, x, y, h, trail, trails, summits):
    trail.append(p := (x, y))
    if h == 9:
        summits.add(p)
        trails.append(trail)
        return
    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        if (nx := x + dx, ny := y + dy) in grid and (nh := grid[nx, ny]) - h == 1:
            explore(grid, nx, ny, nh, [*trail], trails, summits)

with open(argv[1]) as file:
    lines = file.read().splitlines()

grid, trailheads = {}, set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[p := (x, y)] = (h := int(c))
        if not h:
            trailheads.add(p)

n1 = n2 = 0
for thx, thy in trailheads:
    explore(grid, thx, thy, 0, [], trails := [], summits := set())
    n1 += len(summits)
    n2 += len(trails)

print(n1, n2)