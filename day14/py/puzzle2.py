#!/usr/bin/env python

from util import make_cavern, draw_cavern, drip, add_drop

def solve():

    with open('../input.txt', 'r') as f:
        cavern = make_cavern(f)

    sand = {}

    # draw_cavern(cavern, sand, None, True)

    drops = 0
    drop = drip(cavern, sand, True)

    while drop != (500, 0):
        drops += 1

        # if drops % 1000 == 0:
        #     draw_cavern(cavern, sand, drop, True)

        add_drop(sand, drop)

        drop = drip(cavern, sand, True)

    drops += 1 # the last drop
    
    # draw_cavern(cavern, sand, drop, True)

    return drops

if __name__ == "__main__":
    solution = solve()
    print(solution)

