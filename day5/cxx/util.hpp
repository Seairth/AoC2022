#ifndef UTIL_HPP
#define UTIL_HPP

#include<array>
#include<fstream>
#include<regex>
#include<tuple>
#include<vector>

#include "lines.hpp"

#define STACK_COUNT 9

typedef std::vector<std::string> string_vector_t;
typedef std::tuple<string_vector_t, string_vector_t> parts_t;
typedef std::array<std::vector<char>, STACK_COUNT> stacks_t;

parts_t get_parts(std::ifstream& source)
{
    auto mode = 0u;

    string_vector_t stacks;
    string_vector_t commands;

    for (auto& line: lines(source))
    {
        if (line.empty())
        {
            mode++;
            continue;
        }

        switch (mode)
        {
        case 0:
            stacks.push_back(line);
            break;
        
        case 1:
            commands.push_back(line);
            break;
        }
    }

    std::reverse(stacks.begin(), stacks.end());

    return {stacks, commands};
}

stacks_t build_initial_stacks(string_vector_t& lines)
{
    stacks_t stacks {};

    // destructive.  better option would be to use C++20 views
    // to skip the first element
    lines.erase(lines.begin());

    for(auto& line: lines)
    {
        for(auto stack = 0; stack < STACK_COUNT; stack++)
        {
            auto crate = line[stack * 4 + 1];

            if (crate != ' ')
            {
                stacks[stack].push_back(crate);
            }
        }
    }

    return stacks;
}

std::regex r("move ([0-9]+) from ([1-9]) to ([1-9])");

void execute_9000_command(stacks_t& stacks, const std::string& command)
{
    std::smatch match;

    std::regex_search(command, match, r);

    auto crate_count = atoi(match.str(1).c_str());
    auto& from_stack = stacks[atoi(match.str(2).c_str()) - 1];
    auto& to_stack = stacks[atoi(match.str(3).c_str()) - 1];

    for (auto count = 0u; count < crate_count; count++)
    {
        to_stack.push_back(from_stack.back());
        from_stack.pop_back();
    }
}

void execute_9001_command(stacks_t& stacks, const std::string& command)
{
    std::smatch match;

    std::regex_search(command, match, r);

    auto crate_count = atoi(match.str(1).c_str());
    auto& from_stack = stacks[atoi(match.str(2).c_str()) - 1];
    auto& to_stack = stacks[atoi(match.str(3).c_str()) - 1];

    auto it = from_stack.begin() + (from_stack.size() - crate_count);

    for (auto it2 = it; it2 < from_stack.end(); it2++)
    {
        to_stack.push_back(*it2);
    }

    from_stack.erase(it, from_stack.end());
}

#endif