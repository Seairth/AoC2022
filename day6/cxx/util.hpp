#ifndef UTIL_HPP
#define UTIL_HPP

#include <deque>
#include <fstream>
#include <unordered_set>

bool is_unique(std::deque<char> seq)
{
    std::unordered_set<char> _set(seq.begin(), seq.end());
    return _set.size() == seq.size();
}

auto find_unique_sequence(std::ifstream& f, size_t length)
{
    std::deque<char> seq;
    char d;
    auto chars_read = length;

    for (auto i = 0; i < length; i++)
    {
        f >> d;
        seq.push_back(d);
    }

    while(! is_unique(seq))
    {
        f >> d;
        chars_read++;

        seq.pop_front();
        seq.push_back(d);
    }

    return chars_read;
}

#endif