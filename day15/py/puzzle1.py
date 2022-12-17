#!/usr/bin/env python

import re

input_re = re.compile("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


def solve():
    sensors = {}
    beacons = set()

    manhattan_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

    with open('../input.txt', 'r') as f:
        for line in f:
            matches = input_re.search(line)
            
            sensor = int(matches.group(1)), int(matches.group(2))
            beacon = int(matches.group(3)), int(matches.group(4))

            distance = manhattan_distance(sensor, beacon)

            sensors[sensor] = distance
            beacons.add(beacon)
    
    close_sensors = {}
    min_x = 10_000_000
    max_x = -10_000_000

    for k in sensors.keys():
        d = abs(k[1] - 2_000_000)

        if d <= sensors[k]:
            close_sensors[k] = sensors[k]
            delta_x = sensors[k] - d

            min_x = min(min_x, k[0] - delta_x)
            max_x = max(max_x, k[0] + delta_x)

    print(f"min_x: {min_x}, max_x: {max_x}", flush=True)

    covered = 0

    for x in range(min_x, max_x + 1):
        p = (x, 2_000_000)

        for k, v in close_sensors.items():
            if manhattan_distance(k, p) <= v:
                covered += 1
                break

    return covered - len([b for b in beacons if b[1] == 2_000_000])

if __name__ == "__main__":
    solution = solve()
    print(solution)

