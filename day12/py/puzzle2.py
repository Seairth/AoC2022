#!/usr/bin/env python
from typing import TextIO, Tuple, List

from util import load_terrain, AStar
            
def solve():

    with open('../input.txt', 'r') as f:
        map, start, end = load_terrain(f)
        a_star = AStar(map)

    shortest = len(map) * len(map[0])

    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == 0:
                path_len = a_star.solve((x, y), end)

                if path_len is not None and path_len < shortest:
                    shortest = path_len

    return shortest

if __name__ == "__main__":
    solution = solve()
    print(solution)

