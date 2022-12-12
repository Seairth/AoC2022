#!/usr/bin/env python

from util import load_monkeys


def solve():
    with open('../input.txt', 'r') as f:
        monkeys = load_monkeys(f)   

    for _round in range(0, 20):
        for monkey in monkeys:
            if monkey.inspect():
                monkey.items = [i // 3 for i in monkey.items]
                monkey.act(monkeys)

    sorted_inspections = sorted([m.inspections for m in monkeys])

    return sorted_inspections[-2] * sorted_inspections[-1]

if __name__ == "__main__":
    solution = solve()
    print(solution)

