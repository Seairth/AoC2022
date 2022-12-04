#!/usr/bin/env python

from util import get_range_pair, contains

def solve():
    matches = 0

    with open('../input.txt', 'r') as f:
        for line in f:
            ranges = get_range_pair(line)

            if contains(ranges[0], ranges[1]) or contains(ranges[1], ranges[0]):
                matches += 1

    return matches

if __name__ == "__main__":
    solution = solve()
    print(solution, )

