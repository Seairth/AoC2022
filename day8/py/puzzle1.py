#!/usr/bin/env python

def solve():
    visible_trees = set()

    with open('../input.txt', 'r') as f:
        forest = [l[:-1] for l in f.readlines()]
    
    rows = len(forest)
    cols = len(forest[0])

    for row in range(0, rows):
        # the end trees in the row are always visible
        visible_trees.add((row, 0))
        visible_trees.add((row, cols-1))

        tallest_tree = forest[row][0]

        for col in range(1, cols-1):
            if forest[row][col] > tallest_tree:
                visible_trees.add((row, col))
                tallest_tree = forest[row][col]

        tallest_tree = forest[row][-1]

        for col in range(cols-2, 0, -1):
            if forest[row][col] > tallest_tree:
                visible_trees.add((row, col))
                tallest_tree = forest[row][col]

    for col in range(0, cols):
        # the end trees in the col are always visible
        visible_trees.add((0, col))
        visible_trees.add((rows-1, col))

        tallest_tree = forest[0][col]

        for row in range (1, rows-1):
            if forest[row][col] > tallest_tree:
                visible_trees.add((row, col))
                tallest_tree = forest[row][col]

        tallest_tree = forest[-1][col]

        for row in range(rows-2, 0, -1):
            if forest[row][col] > tallest_tree:
                visible_trees.add((row, col))
                tallest_tree = forest[row][col]

    return len(visible_trees)

if __name__ == "__main__":
    solution = solve()
    print(solution, )

