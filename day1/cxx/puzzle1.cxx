#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "lines.hpp"

using namespace std;

const uint32_t solve()
{
    vector<uint32_t> calories = {0};

    ifstream f{"../input.txt"};

    for (auto & line: lines(f))
    {
        if (line.empty())
            calories.push_back(0);
        else
            calories.back() += atoi(line.c_str());
    }

    // the following four lines could probably be replaced by a single line with C++20 std::ranges::max()
    auto max_value = 0u;

    for (auto & c: calories)
    {
        max_value = max(max_value, c);
    }

    return max_value;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}