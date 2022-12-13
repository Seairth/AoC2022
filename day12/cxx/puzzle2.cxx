#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "range.hpp"
#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto terrain = load_terrain(f);
    auto map = std::get<0>(terrain);
    auto end = std::get<2>(terrain);

    AStar a_star {map};

    auto shortest = map.size() * map[0].size();

    for (auto y: iter_range(0, map.size()))
    {
        for (auto x: iter_range(0, map[y].size()))
        {
            if (map[y][x] == 0)
            {
                auto path_len = a_star.solve({x, y}, end);

                if (path_len > 0 && path_len < shortest)
                {
                    shortest = path_len;
                }

            }
        }
    }

    return shortest;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}