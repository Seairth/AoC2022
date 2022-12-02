#include <algorithm>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>

#include "lines.hpp"

using namespace std;

static unordered_map<string, uint32_t> win_lose {
    {"A X", 3}, {"A Y", 6}, {"A Z", 0},
    {"B X", 0}, {"B Y", 3}, {"B Z", 6},
    {"C X", 6}, {"C Y", 0}, {"C Z", 3},
};

const auto solve()
{
    ifstream f{"../input.txt"};

    auto score = 0u;

    for (auto & line: lines(f))
    {
        auto choice = (line[2] - 'X' + 1);
        auto outcome = win_lose[line.substr(0,3)]; 
        score += choice + outcome;
    }

    return score;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}