#!/usr/bin/env python

def solve():
    sum_sig_strengths = 0
    check_sig_at_cycle = 20

    cycle = 1
    x_register = 1

    with open('../input.txt', 'r') as f:
        for line in f:
            if cycle == check_sig_at_cycle:
                sum_sig_strengths += (check_sig_at_cycle * x_register)
                check_sig_at_cycle += 40

            if line[0:4] == 'addx':
                cycle += 1

                if cycle == check_sig_at_cycle:
                    sum_sig_strengths += (check_sig_at_cycle * x_register)
                    check_sig_at_cycle += 40

                x_register += int(line[5:])

            cycle += 1

    return sum_sig_strengths

if __name__ == "__main__":
    solution = solve()
    print(solution)

