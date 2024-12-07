# --- Day 7: Bridge Repair ---

from itertools import product
from operator import add, mul
from sys import argv

def solve(equation, operator_set, retain_unsolvable = False):
    result, *operands = equation
    for operators in product(operator_set, repeat=len(operands) - 1):
        a = operands[0]
        for b, op in zip(operands[1:], operators):
            a = op(a, b)
        if a == result:
            return result
    if retain_unsolvable:
        still_to_be_solved.append(equation)
    return 0

def join(a, b):
    # return int(str(a) + str(b))               # veeeeery slow
    # return 10 ** (int(log10(b)) + 1) * a + b  # better
    k = 10                                      #
    while k <= b:                               #
        k *= 10                                 # faster ;-)
    return k * a + b                            #

with open(argv[1]) as file:
    equations = tuple(tuple(map(int, line.split())) for line in file.read().replace(":", "").splitlines())

still_to_be_solved = []

n1 = sum(solve(e, operator_set=(add, mul), retain_unsolvable=True) for e in equations)
n2 = n1 + sum(solve(e, operator_set=(add, mul, join)) for e in still_to_be_solved)

print(n1, n2)