#!/usr/bin/env python

from util import is_correctly_ordered_lists

def is_correctly_ordered_pair(pair) -> bool:
    left = eval(pair[0])
    right = eval(pair[1])

    return is_correctly_ordered_lists(left, right) >= 0


def solve():
    total = 0
    pair_index = 1

    with open('../input.txt', 'r') as f:

        input_iter = iter(f)

        while True:
            pair = (next(input_iter), next(input_iter))

            if is_correctly_ordered_pair(pair):
                total += pair_index

            if next(input_iter, None) is None:
                break

            pair_index += 1

    return total

if __name__ == "__main__":
    solution = solve()
    print(solution)

