#include <fstream>
#include <iostream>

#include "_atoi.hpp"
#include "lines.hpp"

using namespace std;

auto print_pixel(int32_t crt, int32_t x_register)
{
    auto pixel = ((x_register - 1) <= crt && crt <= (x_register + 1)) ? '#' : '.';
    cout << pixel;

    crt = (crt+1) % 40;

    if (crt == 0)
    {
        cout << endl;
    }

    return crt;
}

const void solve()
{
    auto crt = 0;
    auto x_register = 1;

    ifstream f{"../input.txt"};

    for (auto & line: lines(f))
    {
        crt = print_pixel(crt, x_register);

        auto addend = 0;

        if (line.find("addx") == 0)
        {
            crt = print_pixel(crt, x_register);

            addend = _atoi(line.begin() + 5, line.end());
        }

        x_register += addend;
    }
}

int main()
{
    solve();
}