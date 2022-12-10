#!/usr/bin/env python

from typing import Dict

from util import generate_tree, get_dir_size

def find_small_dirs_total_size(dir: Dict, size_limit: int):
    dir_size = get_dir_size(dir)
    
    if dir_size > size_limit:
        dir_size = 0
    
    for value in dir.values():
        if isinstance(value, dict):
            dir_size += find_small_dirs_total_size(value, size_limit)

    return dir_size

def solve():

    with open('../input.txt', 'r') as f:
        tree = generate_tree(f)

    return find_small_dirs_total_size(tree, 100000)

if __name__ == "__main__":
    solution = solve()
    print(solution, )

