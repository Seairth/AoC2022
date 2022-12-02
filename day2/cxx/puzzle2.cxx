#include <algorithm>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>

#include "lines.hpp"

using namespace std;

static unordered_map<string, char> lose_draw_win {
    {"A X", 'C'}, {"A Y", 'A'}, {"A Z", 'B'},
    {"B X", 'A'}, {"B Y", 'B'}, {"B Z", 'C'},
    {"C X", 'B'}, {"C Y", 'C'}, {"C Z", 'A'},
};

const auto solve()
{
    ifstream f{"../input.txt"};

    auto score = 0u;

    for (auto & line: lines(f))
    {
        auto choice = (lose_draw_win[line.substr(0,3)] - 'A' + 1);
        auto outcome = ((line[2] - 'X') * 3); 
        score += choice + outcome;
    }

    return score;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}