#!/usr/bin/env python
from typing import TextIO, Tuple, List


def load_terrain(f: TextIO) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    start = None
    end = None

    map = []

    for line in f:
        _start = line.find('S')

        if _start >= 0:
            start = (_start, len(map))
            line = line[:_start] + 'a' + line[(_start + 1):]

        _end = line.find('E')

        if _end >= 0:
            end = (_end, len(map))
            line = line[:_end] + 'z' + line[(_end + 1):]

        elevations = [(ord(x) - ord('a')) for x in line[:-1]]
    
        map.append(elevations)
    
    return map, start, end

class AStar:
    def __init__(self, map: List[List[int]]) -> None:
        self.map = map

    def _get_elevation(self, position: Tuple[int, int]) -> int:
        return self.map[position[1]][position[0]]

    def _get_adjacent(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        adjacent = []

        elevation = self._get_elevation(position)

        row = self.map[position[1]]

        if position[0] > 0:
            candidate = (position[0] - 1, position[1])

            if self._get_elevation(candidate) <= elevation + 1:
                adjacent.append(candidate)

        if position[0] < (len(row) - 1):
            candidate = (position[0] + 1, position[1])

            if self._get_elevation(candidate) <= elevation + 1:
                adjacent.append(candidate)

        if position[1] > 0:
            candidate = (position[0], position[1] - 1)

            if self._get_elevation(candidate) <= elevation + 1:
                adjacent.append(candidate)

        if position[1] < (len(self.map) - 1):
            candidate = (position[0], position[1] + 1)

            if self._get_elevation(candidate) <= elevation + 1:
                adjacent.append(candidate)

        return adjacent


    def solve(self, start: Tuple[int, int], end: Tuple[int, int]) -> int :
        open_set = set([start])
        closed_set = set([])

        g = {}
        g[start] = 0

        parents = {}
        parents[start] = start

        while len(open_set) > 0:
            n = None

            for v in open_set:
                if n is None or g[v]< g[n]:
                    n = v

            if n is None:
                return None
            
            if n == end:
                path_len = 0

                while parents[n] != n:
                    path_len += 1
                    n = parents[n]
            
                return path_len

            for m in self._get_adjacent(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + 1

                else:
                    if g[m] > g[n] + 1:
                        g[m] = g[n] + 1
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
            
            open_set.remove(n)
            closed_set.add(n)
