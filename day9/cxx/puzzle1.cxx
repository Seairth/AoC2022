#include <iostream>

#include "util.hpp"

using namespace std;

const auto solve()
{
    return simulate_rope(2);
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}