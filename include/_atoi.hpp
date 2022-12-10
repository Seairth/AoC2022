#ifndef _ATOI_HPP
#define _ATOI_HPP

#include<algorithm>
#include<string>
#include<tuple>

typedef std::tuple<uint32_t, uint16_t> range;
typedef std::tuple<range, range> range_pair;

uint32_t _atoi(std::string::const_iterator begin, const std::string::const_iterator& end)
{
    auto val = 0u;
    auto neg = (*begin == '-');

    if (neg) {
        begin++;
    }

    while (begin != end )
    {
        val = (val * 10) + (*begin - '0');
        begin++;
    }

    if (neg)
    {
        val *= -1;
    }

    return val;
}

#endif