#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

#include "lines.hpp"
#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto sum_priorities = 0u;
    auto num_line = 0u;

    set<char> common;

    for (auto & line: lines(f))
    {
        string items = line;

        if (num_line == 0)
        {
            common.clear();
            common.insert(items.begin(), items.end());
        }
        else
        {
            set<char> temp(items.begin(), items.end());
            set<char> result;

            set_intersection(
                common.begin(), common.end(),
                temp.begin(), temp.end(),
                inserter(result, result.end()));

            common.swap(result);
        }

        num_line = (num_line + 1) % 3;

        if (num_line == 0)
        {
            const auto v = *common.begin();
            sum_priorities += get_priority(v);
        }
    }

    return sum_priorities;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}