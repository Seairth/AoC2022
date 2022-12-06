#include <fstream>
#include <iostream>

#include "util.hpp"

using namespace std;

const auto solve()
{
    ifstream f{"../input.txt"};

    return find_unique_sequence(f, 14);
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}