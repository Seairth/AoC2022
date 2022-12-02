#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "lines.hpp"

using namespace std;

const uint32_t solve()
{
    ifstream f{"../input.txt"};

    for (auto & line: lines(f))
    {
        // do something with the data
    }

    return 0;
}

int main()
{
    auto solution = solve();
    cout << solution << endl;
}