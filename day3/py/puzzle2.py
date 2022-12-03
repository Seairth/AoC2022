#!/usr/bin/env python

from util import get_priority

def solve():

    with open('../input.txt', 'r') as f:
        sum_priorities = 0

        num_line = 0

        for line in f:
            line = line.strip() # remove newline, if present
        
            if num_line == 0:
                common = set(line)
            else:
                common = common.intersection(set(line))

            num_line = (num_line + 1) % 3

            if num_line == 0:
                sum_priorities += get_priority(common.pop())


    return sum_priorities

if __name__ == "__main__":
    solution = solve()
    print(solution, )

