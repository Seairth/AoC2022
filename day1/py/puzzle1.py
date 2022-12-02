#!/usr/bin/env python

def solve():
    calories = [0]

    with open('../input.txt', 'r') as f:
        for line in f:
            if line == "\n":
                calories.append(0)
            else:
                calories[-1] += int(line)

    return max(calories)

if __name__ == "__main__":
    solution = solve()
    print(solution, )

