#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto terrain = load_terrain(f);

    AStar a_star {std::get<0>(terrain)};

    return a_star.solve(std::get<1>(terrain), std::get<2>(terrain));
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}