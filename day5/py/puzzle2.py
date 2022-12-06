#!/usr/bin/env python

from util import get_parts, build_initial_stacks, execute_9001_command

def solve():
    with open('../input.txt', 'r') as f:
        (initial_stacks, commands) = get_parts(f)

        stacks = build_initial_stacks(initial_stacks)

        for command in commands:
            stacks = execute_9001_command(stacks, command)

    top_crates = ''

    for stack in stacks:
        top_crates += stack[-1]

    return top_crates

if __name__ == "__main__":
    solution = solve()
    print(solution, )

