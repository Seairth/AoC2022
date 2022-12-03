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

        auto comp_1 = items.substr(0, num_items);
        auto comp_2 = items.substr(num_items);

        set<char> comp_1_set{comp_1.begin(), comp_1.end()};
        set<char> comp_2_set{comp_2.begin(), comp_2.end()};

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