#!/usr/bin/env python

from util import get_range_pair, overlaps

def solve():
    matches = 0

    with open('../input.txt', 'r') as f:
        for line in f:
            if overlaps(*get_range_pair(line)):
                matches += 1

    return matches

if __name__ == "__main__":
    solution = solve()
    print(solution, )

