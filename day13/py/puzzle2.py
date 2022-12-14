#!/usr/bin/env python

from functools import cmp_to_key
from util import is_correctly_ordered_lists

def is_correctly_ordered_pair(pair) -> bool:
    left = eval(pair[0])
    right = eval(pair[1])

    return is_correctly_ordered_lists(left, right) >= 0


def solve():
    packets = [
        [[2]],
        [[6]]
    ]

    with open('../input.txt', 'r') as f:
        for line in f:
            if len(line) > 1:
                packets.append(eval(line))

    packets.sort(key=cmp_to_key(is_correctly_ordered_lists), reverse=True)

    for divider_1 in range(len(packets)):
        if is_correctly_ordered_lists(packets[divider_1], [[2]]) == 0:
            break

    for divider_2 in range(divider_1, len(packets)):
        if is_correctly_ordered_lists(packets[divider_2], [[6]]) == 0:
            break

    return (divider_1 + 1) * (divider_2 + 1)

if __name__ == "__main__":
    solution = solve()
    print(solution)

