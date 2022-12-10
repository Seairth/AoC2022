#!/usr/bin/env python

def print_pixel(crt, x_register):
    if (x_register - 1) <= crt <= (x_register + 1):
        print('#', end='')
    else:
        print('.', end='')

    crt = (crt + 1) % 40

    if crt == 0:
        print('')

    return crt

def solve():
    crt = 0
    x_register = 1

    with open('../input.txt', 'r') as f:
        for line in f:
            crt = print_pixel(crt, x_register)

            v = 0

            if line[0:4] == 'addx':
                crt = print_pixel(crt, x_register)

                v = int(line[5:])

            x_register += v


if __name__ == "__main__":
    solve()

