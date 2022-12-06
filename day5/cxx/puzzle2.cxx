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

    auto parts = get_parts(f);

    auto stacks = build_initial_stacks(std::get<0>(parts));

    for (auto command: std::get<1>(parts))
    {
        execute_9001_command(stacks, command);
    }

    auto top_crates = ""s;

    for (auto stack: stacks)
    {
        top_crates += stack.back();
    }

    return top_crates;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}