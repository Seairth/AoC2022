#ifndef TRIM_HPP
#define TRIM_HPP


// Credit: https://stackoverflow.com/a/6500499

#include <string>

inline std::string trim(std::string& str)
{
    str.erase(str.find_last_not_of(' ')+1);         //suffixing spaces
    str.erase(0, str.find_first_not_of(' '));       //prefixing spaces
    return str;
}

inline std::string trim(std::string&& str)
{
    auto new_str = str;
    new_str.erase(new_str.find_last_not_of(' ')+1);         //suffixing spaces
    new_str.erase(0, new_str.find_first_not_of(' '));       //prefixing spaces
    return new_str;
}

#endif