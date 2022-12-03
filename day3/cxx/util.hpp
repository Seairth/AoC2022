#ifndef UTIL_HPP
#define UTIL_HPP

auto get_priority(char item)
{
    auto priority_base = 'a' - 1;

    if ('A' <= item && item <= 'Z')
    {
        priority_base = 'A' - 27;
    }

    return (item - priority_base);
}

#endif