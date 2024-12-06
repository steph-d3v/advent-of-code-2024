# --- Day 3: Mull It Over ---

from re import compile
from sys import argv

MUL = compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do(n't)?)\(\)")

n1, n2, ok = 0, 0, True
for a, b, do, _ in MUL.findall(open(argv[1]).read()):
    if do:
        ok = do == "do"
    else:
        n1 += (p := int(a) * int(b))
        n2 += p * ok

print(n1, n2)