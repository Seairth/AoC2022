#ifndef UTIL_HPP
#define UTIL_HPP

#include <fstream>
#include <tuple>
#include <set>
#include <vector>

#include "_atoi.hpp"
#include "lines.hpp"

using position_t = std::tuple<int32_t, int32_t>;

void update_tail_recursive(size_t head_index, std::vector<position_t>& rope, std::set<position_t>& visited)
{
    auto head = rope[head_index];
    auto tail = rope[head_index + 1];

    auto x_distance = abs(std::get<0>(head) - std::get<0>(tail));
    auto y_distance = abs(std::get<1>(head) - std::get<1>(tail));

    if (x_distance > 1 || y_distance > 1)
    {
        if (std::get<0>(head) == std::get<0>(tail))
        {
            // same col
            auto delta = (std::get<1>(head) > std::get<1>(tail)) ? 1 : -1;
            tail = { std::get<0>(tail), std::get<1>(tail) + delta };
        }
        else if (std::get<1>(head) == std::get<1>(tail))
        {
            // same row
            auto delta = (std::get<0>(head) > std::get<0>(tail)) ? 1 : -1;
            tail = { std::get<0>(tail) + delta, std::get<1>(tail) };
        }
        else
        {
            // diagonal
            auto x_delta = (std::get<0>(head) > std::get<0>(tail)) ? 1 : -1;
            auto y_delta = (std::get<1>(head) > std::get<1>(tail)) ? 1 : -1;
            
            tail = { std::get<0>(tail) + x_delta, std::get<1>(tail) + y_delta };
        }

        rope[head_index + 1] = tail;

        if (head_index + 1 == rope.size() - 1)
        {
            visited.insert(tail);
        }
        else
        {
            update_tail_recursive(head_index + 1, rope, visited);
        }
    } 
}

auto simulate_rope(size_t rope_len)
{
    std::vector<position_t> rope;

    for (auto i = 0; i < rope_len; i++)
    {
        rope.push_back({0, 0});
    }

    std::set<position_t> visited { rope.back() };

    std::ifstream f{"../input.txt"};

    for (auto & line: lines(f))
    {
        auto direction = line[0];
        auto distance = _atoi(line.begin() + 2, line.end());

        for (auto step = 0; step < distance; step++)
        {
            auto head = rope[0];

            switch (direction)
            {
            case 'U':
                head = {std::get<0>(head), std::get<1>(head) + 1};
                break;
            
            case 'D':
                head = {std::get<0>(head), std::get<1>(head) - 1};
                break;

            case 'R':
                head = {std::get<0>(head) + 1, std::get<1>(head)};
                break;

            case 'L':
                head = {std::get<0>(head) - 1, std::get<1>(head)};
                break;
            }

            rope[0] = head;

            update_tail_recursive(0, rope, visited);
        }
    }

    return visited.size();
}

#endif