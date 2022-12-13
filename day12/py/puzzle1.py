#!/usr/bin/env python
from typing import TextIO, Tuple, List

from util import load_terrain, AStar
            
def solve():

    with open('../input.txt', 'r') as f:
        map, start, end = load_terrain(f)
        a_star = AStar(map)

    return a_star.solve(start, end)

if __name__ == "__main__":
    solution = solve()
    print(solution)

