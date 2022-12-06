import re

from typing import List, Tuple, TextIO

def get_parts(source: TextIO) -> Tuple[List[str], List[str]]:
    mode = 0

    stacks = []
    commands = []

    for line in source:
        if line == '\n':
            mode += 1
            continue

        if mode == 0:
            stacks.insert(0, line)
        elif mode == 1:
            commands.append(line)

    return (stacks, commands)


def build_initial_stacks(lines: List[str]) -> List[List[str]]:
    stacks = []

    for stack in range(9):
        stacks.append([])

    for line in lines[1:]:
        for stack in range(9):
            crate = line[stack * 4 + 1]

            if crate != ' ':
                stacks[stack].append(crate)

    return stacks


def execute_9000_command(stacks: List[List[str]], command: str) -> List[List[str]]:
    m = re.search('move ([0-9]+) from ([1-9]) to ([1-9])', command)    

    crate_count = int(m.group(1))
    from_stack = int(m.group(2))
    to_stack = int(m.group(3))

    for count in range(crate_count):
        crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(crate)

    return stacks


def execute_9001_command(stacks: List[List[str]], command: str) -> List[List[str]]:
    m = re.search('move ([0-9]+) from ([1-9]) to ([1-9])', command)    

    crate_count = int(m.group(1))
    from_stack = int(m.group(2))
    to_stack = int(m.group(3))

    crates = stacks[from_stack - 1][-crate_count:]

    for count in range(crate_count):
        stacks[to_stack - 1].append(crates[count])
        stacks[from_stack - 1].pop()

    return stacks
