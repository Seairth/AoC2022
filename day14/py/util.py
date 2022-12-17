from typing import Dict, List, TextIO, Tuple, Union

def make_cavern(f: TextIO) -> Dict[int, List[int]]:
    cavern: Dict[int, List[int]] = {}

    for line in f:
        points = []
        
        for point in line.split(" -> "):
            xy = point.split(",")
            x = int(xy[0])
            y = int(xy[1])
            points.append((x, y))

        for idx in range(len(points) - 1):
            p1 = points[idx]
            p2 = points[idx + 1]

            if p1[0] == p2[0]:
                # vertical line
                if p1[1] > p2[1]:
                    p1, p2 = p2, p1
                
                if not p1[0] in cavern:
                    cavern[p1[0]] = []

                for y in range(p1[1], p2[1] + 1):
                    if not y in cavern[p1[0]]:
                        cavern[p1[0]].append(y)

            elif p1[1] == p2[1]:
                # horizontal line
                if p1[0] > p2[0]:
                    p1, p2 = p2, p1
                
                for x in range(p1[0], p2[0] + 1):
                    if not x in cavern:
                        cavern[x] = []

                    if not p1[1] in cavern[x]:
                        cavern[x].append(p1[1])
            else:
                print(f"Line [{p1}, {p2}] isn't vertical/horizontal. Line: {line}")

    for v in cavern.values():
        v.sort()

    return cavern

def draw_cavern(cavern: Dict[int, List[int]], sand: Dict[int, List[int]], drop: Tuple[int, int], floor = False):
    min_x = min(cavern.keys())
    max_x = max(cavern.keys())

    min_y = min([y[0] for y in cavern.values()])
    max_y = max([y[-1] for y in cavern.values()])

    if len(sand) > 0:
        min_x = min(min_x, min(sand.keys()))
        max_x = max(max_x, max(sand.keys()))

        min_y = min(min_y, min([y[0] for y in sand.values()]))
        max_y = max(max_y, max([y[-1] for y in sand.values()]))

    print("     ", end='')

    for x in range(min_x, max_x + 1):
        if x == 500:
            print('+', end='')
        else:
            print(' ', end='')

    print()
    print("     ", end='')

    for x in range(min_x, max_x + 1):
        if x == 500:
            print(' ', end='')
        else:
            print('_', end='')

    print()

    for y in range(min_y, max_y + 1):
        print(f"{y:03}: ", end='')

        for x in range(min_x, max_x + 1):
            if x in cavern and y in cavern[x]:
                print('#', end='')
            elif x in sand and y in sand[x]:
                print('o', end='')
            elif (x, y) == drop:
                print('@', end='')
            else:
                print('.', end='')
        
        print()

    if floor:
        print(f"{(max_y + 3):03}: ", end='')

        for x in range(min_x, max_x + 1):
            print('#', end='')
        

    print('', flush=True)

def get_obstacle_y(cavern: Dict[int, List[int]], sand: Dict[int, List[int]], drop: Tuple[int, int], floor = False) -> Union[int, None]:
    obstacle_y = None

    if drop[0] in sand and drop[1] < sand[drop[0]][-1]:
        for y in sand[drop[0]]:
            if y > drop[1]:
                obstacle_y = y
                break
    
    if drop[0] in cavern and drop[1] < cavern[drop[0]][-1]:
        for y in cavern[drop[0]]:
            if y > drop[1]:
                obstacle_y = y if obstacle_y is None else min(obstacle_y, y)
                break

    if floor and obstacle_y is None:
        obstacle_y = max([y[-1] for y in cavern.values()]) + 2

    return obstacle_y

def is_left_obstacle(cavern: Dict[int, List[int]], sand: Dict[int, List[int]], drop: Tuple[int, int], floor = False) -> bool:
    left_col = drop[0] - 1
    y = drop[1] + 1

    if left_col in cavern and y in cavern[left_col]:
        return True

    if left_col in sand and y in sand[left_col]:
        return True

    if floor and (max([y[-1] for y in cavern.values()]) + 2) == y:
        return True

    return False

def is_right_obstacle(cavern: Dict[int, List[int]], sand: Dict[int, List[int]], drop: Tuple[int, int], floor = False) -> bool:
    right_col = drop[0] + 1
    y = drop[1] + 1

    if right_col in cavern and y in cavern[right_col]:
        return True

    if right_col in sand and y in sand[right_col]:
        return True

    if floor and (max([y[-1] for y in cavern.values()]) + 2) == y:
        return True

    return False

def drip(cavern: Dict[int, List[int]], sand: Dict[int, List[int]], floor = False) -> Union[Tuple[int, int], None]:
    drop = (500, 0)

    while True:
        obstacle_y = get_obstacle_y(cavern, sand, drop, floor)

        if obstacle_y is None:
            drop = None
            break

        next_drop = (drop[0], obstacle_y - 1)

        if not is_left_obstacle(cavern, sand, next_drop, floor):
            drop = (next_drop[0] - 1, next_drop[1] + 1)
            continue

        if not is_right_obstacle(cavern, sand, next_drop, floor):
            drop = (next_drop[0] + 1, next_drop[1] + 1)
            continue

        drop = next_drop
        break

    return drop

def add_drop(sand: Dict[int, List[int]], drop: Tuple[int, int]):
    if not drop[0] in sand:
        sand[drop[0]] = []

    sand[drop[0]].append(drop[1])
    sand[drop[0]].sort()
