# --- Day 11: Plutonian Pebbles ---

from functools import cache
from sys import argv

@cache
def blink(stone, n):
    if not n:
        return 1
    n -= 1
    if not stone:
        return blink(1, n)
    if not (size := len(s := str(stone))) & 1:
        half = size >> 1
        return blink(int(s[:half]), n) + blink(int(s[half:]), n)
    return blink(stone * 2024, n)

with open(argv[1]) as file:
    stones = map(int, file.read().split())

n1 = n2 = 0

for stone in stones:
    n1 += blink(stone, 25)
    n2 += blink(stone, 75)

print(n1, n2)