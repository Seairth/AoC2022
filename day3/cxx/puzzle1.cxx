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

    for (auto & line: lines(f))
    {
        string items = line;

        auto num_items = items.length() / 2;

        set<char> comp_1_set{items.begin(), items.begin() + num_items};
        set<char> comp_2_set{items.begin() + num_items, items.end()};

        vector<char> common(items.length());

        set_intersection(
            comp_1_set.begin(), comp_1_set.end(),
            comp_2_set.begin(), comp_2_set.end(),
            common.begin());

        sum_priorities += get_priority(common[0]);
    }

    return sum_priorities;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}