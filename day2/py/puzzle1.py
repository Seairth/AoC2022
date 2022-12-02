#!/usr/bin/env python

XYZ = { 'X': 1, 'Y': 2, 'Z': 3}

win_lose = {
    'X': { 'A': 3, 'B': 0, 'C': 6 },
    'Y': { 'A': 6, 'B': 3, 'C': 0 },
    'Z': { 'A': 0, 'B': 6, 'C': 3 }
}

def solve():
    score = 0

    with open('../input.txt', 'r') as f:
        for line in f:
            opponent = line[0]
            player = line[2]

            score += XYZ[player] + win_lose[player][opponent]        

    return score

if __name__ == "__main__":
    solution = solve()
    print(solution, )

