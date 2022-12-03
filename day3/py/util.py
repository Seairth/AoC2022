def get_priority(item):
    priority_base = ord('a') - 1

    if 'A' <= item <= 'Z':
        priority_base = ord('A') - 27

    return ord(item) - priority_base