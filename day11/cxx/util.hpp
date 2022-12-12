#ifndef UTIL_HPP
#define UTIL_HPP

#include <fstream>
#include <iostream>
#include <stdint.h>
#include <string>
#include <vector>

#include "_atoi.hpp"
#include "lines.hpp"
#include "range.hpp"
#include "trim.hpp"

struct Monkey
{
    std::vector<uint64_t> items;
    char op;
    bool op_old_value;
    uint64_t op_value;    
    uint64_t test_value;
    size_t true_monkey;
    size_t false_monkey;
    uint64_t inspections;

    Monkey(std::vector<std::string>& initial_state): op_old_value(false), op_value(0),  inspections(0)
    {
        auto _items = initial_state[1].substr(initial_state[1].find(':') + 2);

        auto _begin = _items.begin();
        auto _current = _begin;

        while (_current != _items.end())
        {
            if (*_current == ',')
            {
                items.push_back(_atoi(_begin, _current));
                _begin = _current + 2;
            }

            _current++;
        }

        items.push_back(_atoi(_begin, _current));

        auto _operation = initial_state[2].substr(initial_state[2].find(':') + 1);

        op = ( _operation.find('*') == _operation.npos) ? '+' : '*';

        auto _op_value = trim(initial_state[2].substr(initial_state[2].find(op) + 1));

        op_old_value = _op_value == "old";

        if (!op_old_value)
        {
            op_value = _atoi(_op_value.begin(), _op_value.end());
        } 
    
        auto _test_value = trim(initial_state[3].substr(initial_state[3].find("by") + 2));

        test_value = _atoi(_test_value.begin(), _test_value.end());

        true_monkey = initial_state[4].back() - '0';
        false_monkey = initial_state[5].back() - '0';
    }

    Monkey(Monkey&& other)
    {
        items = std::move(other.items);

        op = other.op;
        op_old_value = other.op_old_value;
        op_value = other.op_value;
        test_value = other.test_value;
        true_monkey = other.true_monkey;
        false_monkey = other.false_monkey;
        inspections = other.inspections;
    }

    bool inspect()
    {
        if (items.size() == 0)
        {
            return false;
        }

        for (auto i: iter_range(0, items.size()))
        {
            if (op == '*')
            {
                if (op_old_value) {
                    items[i] *= items[i];
                }
                else
                {
                    items[i] *= op_value;
                }
            }
            else
            {
                if (op_old_value)
                {
                    items[i] += items[i];
                }
                else
                {
                    items[i] += op_value;
                }
            }
        }

        inspections += items.size();

        return true;
    }

    void act(std::vector<Monkey>& monkeys)
    {
        for (auto item: items)
        {
            if (item % test_value == 0)
            {
                monkeys[true_monkey].items.push_back(item);
            }
            else
            {
                monkeys[false_monkey].items.push_back(item);
            }
        }

        items.clear();
    }
};


auto load_monkeys(std::ifstream& f)
{
    std::vector<Monkey> monkeys;

    auto line_count = 0;
    std::vector<std::string> _lines;

    for (auto & line: lines(f))
    {
        _lines.push_back(line);

        line_count = (line_count + 1) % 7;

        if (line_count == 0)
        {
            monkeys.push_back({_lines});
            _lines.clear();
        }
    }

    if (_lines.size() > 0)
    {
        monkeys.push_back({_lines});
    }

    return monkeys;
}

#endif
