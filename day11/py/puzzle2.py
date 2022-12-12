#!/usr/bin/env python

from util import load_monkeys
from functools import reduce

def solve():
    with open('../input.txt', 'r') as f:
        monkeys = load_monkeys(f)   

    limit = reduce(lambda a, b: a * b, [m.test_value for m in monkeys])

    for _round in range(0, 10_000):
        for monkey in monkeys:
            if monkey.inspect():
                monkey.items = [i % limit for i in monkey.items]
                monkey.act(monkeys)

    sorted_inspections = sorted([m.inspections for m in monkeys])

    return sorted_inspections[-2] * sorted_inspections[-1]

if __name__ == "__main__":
    solution = solve()
    print(solution)

