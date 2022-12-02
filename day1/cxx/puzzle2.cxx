#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
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

    sort(calories.begin(), calories.end());

    return accumulate(calories.end()-3, calories.end(), 0u);
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}