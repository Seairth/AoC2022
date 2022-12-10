#!/usr/bin/env python

from typing import Dict

from util import generate_tree, get_dir_size

def find_all_dir_sizes(dir: Dict):
    dir_sizes = []

    dir_size = get_dir_size(dir)
    
    for value in dir.values():
        if isinstance(value, dict):
            dir_sizes.extend(find_all_dir_sizes(value))

    dir_sizes.append(dir_size)

    return dir_sizes

def solve():

    with open('../input.txt', 'r') as f:
        tree = generate_tree(f)

    root_size = get_dir_size(tree)
    unused_space = 70_000_000 - root_size

    amount_needed = 30_000_000 - unused_space

    sizes = sorted(find_all_dir_sizes(tree))

    for size in sizes:
        if size > amount_needed:
            break

    return size

if __name__ == "__main__":
    solution = solve()
    print(solution, )

