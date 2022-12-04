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
        // apply passes the tuple returned by `get_range_pair` as arguments to `overlaps`
        if(apply(overlaps, get_range_pair(line)))
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