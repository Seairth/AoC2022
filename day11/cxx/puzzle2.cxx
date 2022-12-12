#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

#include "range.hpp"
#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    auto monkeys = load_monkeys(f);

    auto limit = std::transform_reduce(
        monkeys.cbegin(),
        monkeys.cend(),
        1ull,
        std::multiplies{},
        [](const Monkey& m) { return m.test_value; }
    );

    for (auto _round: iter_range(0, 10'000))
    {
        for (auto& monkey: monkeys)
        {
            if (monkey.inspect())
            {
                std::transform(
                    monkey.items.cbegin(),
                    monkey.items.cend(),
                    monkey.items.begin(),
                    [=](const uint64_t v) { return v % limit; } 
                );

                monkey.act(monkeys);
            }
        }
    }


    vector<uint64_t> inspections(monkeys.size());

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