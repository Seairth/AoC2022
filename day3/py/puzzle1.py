#!/usr/bin/env python

from util import get_priority

def solve():

    with open('../input.txt', 'r') as f:
        sum_priorities = 0

        for line in f:
            line = line.strip() # remove newline, if present

            num_items = int(len(line)/2)
            
            comp_1 = line[:num_items]
            comp_2 = line[num_items:]

            common = set(comp_1).intersection(set(comp_2)).pop()

            sum_priorities += get_priority(common)

    return sum_priorities

if __name__ == "__main__":
    solution = solve()
    print(solution, )

