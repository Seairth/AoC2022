#ifndef UTIL_HPP
#define UTIL_HPP

#include<algorithm>
#include<string>
#include<tuple>

typedef std::tuple<uint32_t, uint16_t> range;
typedef std::tuple<range, range> range_pair;

uint32_t _atoi(std::string::const_iterator begin, const std::string::const_iterator& end)
{
    auto val = 0u;

    while (begin != end )
    {
        val = (val * 10) + (*begin - '0');
        begin++;
    }

    return val;
}


const range_pair get_range_pair(const std::string& line)
{
    auto comma = std::find(line.begin(), line.end(), ',');
    auto dash_1 = std::find(line.begin(), comma, '-');
    auto dash_2 = std::find(comma, line.end(), '-');

    const auto r1_min = _atoi(line.begin(), dash_1);
    const auto r1_max = _atoi(dash_1 + 1, comma);
    const auto r1 = std::make_tuple(r1_min, r1_max);

    const auto r2_min = _atoi(comma + 1, dash_2);
    const auto r2_max = _atoi(dash_2 + 1, line.end());
    const auto r2 = std::make_tuple(r2_min, r2_max);

    return {r1, r2};
}

bool contains(const range& range_1, const range& range_2)
{
    return std::get<0>(range_1) <= std::get<0>(range_2) && std::get<1>(range_1) >= std::get<1>(range_2);
}

bool overlaps(const range& range_1, const range& range_2)
{
    // is this going overboard?  yes.  but I wanted to practice using make_tuple().
    auto r_1 = std::make_tuple(std::get<0>(range_1), std::get<0>(range_1));
    auto r_2 = std::make_tuple(std::get<0>(range_2), std::get<0>(range_2));

    return contains(range_1, r_2) || contains(std::move(range_2), r_1);
}

#endif