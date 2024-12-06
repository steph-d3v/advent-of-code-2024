# --- Day 5: Print Queue ---

from collections import defaultdict
from functools import cmp_to_key
from sys import argv

with open(argv[1]) as file:
    content = file.read()

part1, part2 = content.split("\n\n")

rules = (tuple(map(int, line.split("|"))) for line in part1.splitlines())
updates = (list(map(int, line.split(","))) for line in part2.splitlines())

after = defaultdict(list)
for a, b in rules:
    after[a].append(b)

new_updates = [[], []] # to be sorted, already sorted

def is_sorted(update):
    for i, a in enumerate(update):
        for b in update[i+1:]:
            if a in after[b]:
                return False
    return True

for update in updates:
    new_updates[s := is_sorted(update)].append(
        update if s else sorted(
            update,
            key=cmp_to_key(lambda a, b: -1 if b in after[a] else 1)
        )
    )

n2, n1 = map(lambda updated: sum(u[len(u)//2] for u in updated), new_updates)

print(n1, n2)