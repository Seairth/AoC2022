#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

#include "range.hpp"
#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto monkeys = load_monkeys(f);

    for (auto _round: iter_range(0, 20))
    {
        for (auto& monkey: monkeys)
        {
            if (monkey.inspect())
            {
                std::transform(
                    monkey.items.cbegin(),
                    monkey.items.cend(),
                    monkey.items.begin(),
                    [](const uint64_t v) { return v / 3ull; } 
                );

                monkey.act(monkeys);
            }
        }
    }


    vector<uint32_t> inspections(monkeys.size());

    std::transform(
        monkeys.cbegin(),
        monkeys.cend(),
        inspections.begin(),
        [](const Monkey& monkey) { return monkey.inspections; }
    );

    std::sort(inspections.begin(), inspections.end());

    auto v1 = *(inspections.rbegin());
    auto v2 = *(inspections.rbegin() + 1);

    return v1 * v2;    
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}