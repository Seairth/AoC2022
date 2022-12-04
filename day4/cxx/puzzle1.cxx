#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "lines.hpp"
#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto matches = 0u;

    for (auto & line: lines(f))
    {
        auto ranges = get_range_pair(line);

        if (contains(get<0>(ranges), get<1>(ranges)) || contains(get<1>(ranges), get<0>(ranges)))
        {
            matches++;
        }
    }

    return matches;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}