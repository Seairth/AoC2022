#!/usr/bin/env python

def view_left(forest, row, col):
    
    if col == 0:
        return 0
    
    for _c in range(col-1, -1, -1):
        if forest[row][_c] >= forest[row][col]:
            break

    return (col - _c)


def view_right(forest, row, col):
    
    if col == (len(forest[row]) - 1):
        return 0
    
    for _c in range(col+1, len(forest[row])):
        if forest[row][_c] >= forest[row][col]:
            break

    return (_c - col)

def view_up(forest, row, col):
    
    if row == 0:
        return 0
    
    for _r in range(row-1, -1, -1):
        if forest[_r][col] >= forest[row][col]:
            break

    return (row - _r)

def view_down(forest, row, col):
    
    if row == (len(forest) - 1):
        return 0
    
    for _r in range(row+1, len(forest)):
        if forest[_r][col] >= forest[row][col]:
            break

    return (_r - row)

def solve():
    most_visible_trees = 0

    with open('../input.txt', 'r') as f:
        forest = [l[:-1] for l in f.readlines()]
    
    rows = len(forest)
    cols = len(forest[0])

    for row in range(0, rows):
        for col in range(0, cols):
            visible_trees = 1
            visible_trees *= view_up(forest, row, col)
            visible_trees *= view_down(forest, row, col)
            visible_trees *= view_left(forest, row, col)
            visible_trees *= view_right(forest, row, col)

            if visible_trees > most_visible_trees:
                most_visible_trees = visible_trees

    return most_visible_trees

if __name__ == "__main__":
    solution = solve()
    print(solution, )

