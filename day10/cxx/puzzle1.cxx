#include <fstream>
#include <iostream>

#include "_atoi.hpp"
#include "lines.hpp"

using namespace std;

const auto solve()
{
    auto sum_sig_strengths = 0;
    auto check_sig_at_cycle = 20;

    auto cycle = 1;
    auto x_register = 1;

    ifstream f{"../input.txt"};

    for (auto & line: lines(f))
    {
        if (cycle == check_sig_at_cycle)
        {
            sum_sig_strengths += (check_sig_at_cycle * x_register);
            check_sig_at_cycle += 40;
        }

        auto addend = 0;

        if (line.find("addx") == 0)
        {
            cycle++;

            if (cycle == check_sig_at_cycle)
            {
                sum_sig_strengths += (check_sig_at_cycle * x_register);
                check_sig_at_cycle += 40;
            }

            addend = _atoi(line.begin() + 5, line.end());
        }
        
        cycle++;

        x_register += addend;
    }

    return sum_sig_strengths;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}