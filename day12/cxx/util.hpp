#ifndef UTIL_HPP
#define UTIL_HPP

#include <fstream>
#include <map>
#include <set>
#include <tuple>
#include <vector>

#include "lines.hpp"

using map_t = std::vector<std::vector<uint32_t>>;
using position_t = std::tuple<uint32_t, uint32_t>;

std::tuple<map_t, position_t, position_t> load_terrain(std::ifstream& f)
{
    position_t start;
    position_t end;

    map_t map;

    for (auto line: lines(f))
    {
        auto _start = line.find('S');

        if (_start != line.npos)
        {
            start = { _start, map.size() };
            line[_start] = 'a';
        }

        auto _end = line.find('E');

        if (_end != line.npos)
        {
            end = { _end, map.size() };
            line[_end] = 'z';
        }

        std::vector<uint32_t> elevations {};

        for (const auto c: line)
        {
            elevations.push_back(c - 'a');
        }

        map.push_back(elevations);
    }

    return { map, start, end };
}


class AStar
{
    private:
        auto get_elevation(const position_t& position)
        {
            return map[std::get<1>(position)][std::get<0>(position)];
        }

        auto get_adjacent(const position_t& position)
        {
            std::vector<position_t> adjacent;

            auto elevation = get_elevation(position);

            auto row = map[std::get<1>(position)];

            if (std::get<0>(position) > 0)
            {
                position_t candidate = { std::get<0>(position) - 1, std::get<1>(position) };

                if (get_elevation(candidate) <= elevation + 1)
                {
                    adjacent.push_back(candidate);
                }
            }

            if (std::get<0>(position) < row.size() - 1)
            {
                position_t candidate = { std::get<0>(position) + 1, std::get<1>(position) };

                if (get_elevation(candidate) <= elevation + 1)
                {
                    adjacent.push_back(candidate);
                }
            }

            if (std::get<1>(position) > 0)
            {
                position_t candidate = { std::get<0>(position), std::get<1>(position) - 1 };

                if (get_elevation(candidate) <= elevation + 1)
                {
                    adjacent.push_back(candidate);
                }
            }

            if (std::get<1>(position) < map.size() - 1)
            {
                position_t candidate = { std::get<0>(position), std::get<1>(position) + 1 };

                if (get_elevation(candidate) <= elevation + 1)
                {
                    adjacent.push_back(candidate);
                }
            }

            return adjacent;
        }

    private:
        map_t map;

        const position_t no_position { -1, -1};

    public:
        AStar(map_t map): map(map) {}

        auto solve(const position_t& start, const position_t& end)
        {
            std::set<position_t> open_set { start };
            std::set<position_t> closed_set {};

            std::map<position_t, uint32_t> g {{start, 0}};

            std::map<position_t, position_t> parents {{start, start}};

            while (open_set.size() > 0)
            {
                auto n = no_position;

                for (auto& v: open_set)
                {
                    if (n == no_position || g[v] < g[n])
                    {
                        n = v;
                    }
                }

                if (n == no_position)
                {
                    break;
                }

                if (n == end)
                {
                    auto path_len = 0u;

                    while (parents[n] != n)
                    {
                        path_len++;
                        n = parents[n];
                    }

                    return path_len;
                }

                for (auto m: get_adjacent(n))
                {
                    if (open_set.find(m) == open_set.end() && closed_set.find(m) == closed_set.end())
                    {
                        open_set.insert(m);
                        parents[m] = n;
                        g[m] = g[n] + 1;
                    }
                    else
                    {
                        if (g[m] > g[n] + 1)
                        {
                            g[m] = g[n] + 1;
                            parents[m] = n;

                            if (closed_set.find(m) != closed_set.end())
                            {
                                closed_set.erase(m);
                                open_set.insert(m);
                            }
                        }
                    }
                }

                open_set.erase(n);
                closed_set.insert(n);
            }

            return 0u;
        }
};

#endif