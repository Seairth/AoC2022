#!/usr/bin/env python


from util import make_cavern, draw_cavern, drip, add_drop

def solve():

    with open('../input.txt', 'r') as f:
        cavern = make_cavern(f)

    sand = {}

    # draw_cavern(cavern, sand, None)

    drops = 0
    drop = drip(cavern, sand)

    while drop is not None:
        drops += 1

        # draw_cavern(cavern, sand, drop)

        add_drop(sand, drop)

        drop = drip(cavern, sand)

    # draw_cavern(cavern, sand, drop)

    return drops

if __name__ == "__main__":
    solution = solve()
    print(solution)

