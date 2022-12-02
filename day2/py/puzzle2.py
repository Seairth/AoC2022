#!/usr/bin/env python

ABC = { 'A': 1, 'B': 2, 'C': 3}
XYZ = { 'X': 0, 'Y': 3, 'Z': 6}

lose_draw_win = {
    'X': { 'A': 'C', 'B': 'A', 'C': 'B' },
    'Y': { 'A': 'A', 'B': 'B', 'C': 'C' },
    'Z': { 'A': 'B', 'B': 'C', 'C': 'A' }
}

def solve():
    score = 0

    with open('../input.txt', 'r') as f:
        for line in f:
            opponent = line[0]
            outcome = line[2]

            score += ABC[lose_draw_win[outcome][opponent]] + XYZ[outcome]        

    return score

if __name__ == "__main__":
    solution = solve()
    print(solution, )

