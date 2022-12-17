#!/usr/bin/env python

import re

input_re = re.compile("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

def solve():
    sensors = {}

    manhattan_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

    with open('../input.txt', 'r') as f:
        for line in f:
            matches = input_re.search(line)
            
            sensor = int(matches.group(1)), int(matches.group(2))
            beacon = int(matches.group(3)), int(matches.group(4))

            sensors[sensor] = manhattan_distance(sensor, beacon)

    empty_spot = None

    keys = tuple(sensors.keys())

    for idx in range(len(keys)):
        k = keys[idx]
        v = sensors[k]

        md = v + 1

        for x_offset in range(md, 0):
            x = k[0] + x_offset

            if 0 <= x <= 4_000_000:
                y = k[1] + (md + x_offset)

                if  0 <= y <= 4_000_000:  
                    point = (x, y)
                    
                    if not any([manhattan_distance(point, _key) <= sensors[_key] for _key in keys if _key != k]):
                        empty_spot = point
                        break

                y = k[1] - (md + x_offset)

                if 0 <= y <= 4_000_000:  
                    point = (x, y)
                    
                    if not any([manhattan_distance(point, _key) <= sensors[_key] for _key in keys if _key != k]):
                        empty_spot = point
                        break

        else:
            for x_offset in range(0, md + 1):
                x = k[0] + x_offset

                if 0 <= x <= 4_000_000:  
                    y = k[1] + (md - x_offset)

                    if 0 <= y <= 4_000_000:  
                        point = (x, y)
                        
                        if not any([manhattan_distance(point, _key) <= sensors[_key] for _key in keys if _key != k]):
                            empty_spot = point
                            break

                    y = k[1] - (md - x_offset)

                    if 0 <= y <= 4_000_000:  
                        point = (x, y)
                        
                        if not any([manhattan_distance(point, _key) <= sensors[_key] for _key in keys if _key != k]):
                            empty_spot = point
                            break

    return (empty_spot[0] * 4_000_000) + empty_spot[1]

if __name__ == "__main__":
    solution = solve()
    print(solution)

