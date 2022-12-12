from typing import List, TextIO, Callable

class InvalidOperation(Exception): pass

class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.operation = lambda x: x
        self.test_value = -1
        self.true_monkey = -1
        self.false_monkey = -1
        self.inspections = 0

    def inspect(self) -> bool:
        if len(self.items) == 0:
            return False

        self.items = [self.operation(i) for i in self.items]
        self.inspections += len(self.items)

        return True

    def act(self, monkeys: List["Monkey"]):
        if len(self.items) == 0:
            raise InvalidOperation

        for item in self.items:
            if item % self.test_value == 0:
                monkeys[self.true_monkey].items.append(item)
            else:
                monkeys[self.false_monkey].items.append(item)

        self.items = []

def _make_mul_func(operand) -> Callable:
    if operand == 'old':
        return lambda x: x * x

    v = int(operand)
    return lambda x: x * v

def _make_add_func(operand) -> Callable:
    if operand == 'old':
        return lambda x: x + x
    
    v = int(operand)
    return lambda x: x + v

def load_monkey(initial_state: List[str]) -> Monkey:
    monkey = Monkey()

    items = initial_state[1].split(':')[1]
    
    monkey.items = [int(i.strip()) for i in items.split(',')]

    operation = initial_state[2].split(':')[1]

    if '*' in operation:
        operand = operation.split('*')[1].strip()
        monkey.operation = _make_mul_func(operand)
    else:
        operand = operation.split('+')[1]
        monkey.operation = _make_add_func(operand)

    test_value = int(initial_state[3].split('by')[1].strip())

    monkey.test_value = test_value

    monkey.true_monkey = int(initial_state[4][-2])
    monkey.false_monkey = int(initial_state[5][-2])   

    return monkey

def load_monkeys(f: TextIO) -> List[Monkey]:
    monkeys = []

    line_count = 0
    lines = []

    for line in f:
        lines.append(line)

        line_count = (line_count + 1) % 7

        if line_count == 0:
            monkeys.append(load_monkey(lines))
            lines.clear()

    if len(lines) > 0:
        monkeys.append(load_monkey(lines))

    return monkeys