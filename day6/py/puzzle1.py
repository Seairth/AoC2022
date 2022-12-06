#!/usr/bin/env python

from util import find_unique_sequence

def solve():

    with open('../input.txt', 'r') as f:
        return find_unique_sequence(f, 4)

if __name__ == "__main__":
    solution = solve()
    print(solution, )

