from typing import Dict

def generate_tree(data) -> Dict:
    root = {}
    current_dir = root
    dir_stack = [root]

    for line in data:
        if line[0] == '$':
            if line[2:4] == 'cd':
                path = line[5:-1]

                if path == '/':
                    dir_stack = [root]
                elif path == '..':
                    dir_stack.pop()
                else:
                    dir_stack.append(current_dir[path])
                
                current_dir = dir_stack[-1]
            else:
                # ls command.  Ignore.
                pass
        else:
            entry = line.split(' ')
            entry_name = entry[1][:-1] # remove \n

            if entry[0] == 'dir':
                current_dir[entry_name] = {}
            else:
                current_dir[entry_name] = int(entry[0])

    return root

def print_tree(tree: Dict, indent = 0):
    for (key, value) in tree.items():
        if isinstance(value, dict):
            print(' ' * indent, '-', key,)
            print_tree(value, indent + 2)
        else:
            print(' ' * indent, '-', key, '(size:', value, ')',)

def get_dir_size(dir: Dict):
    size = 0

    for value in dir.values():
        if isinstance(value, dict):
            size += get_dir_size(value)
        else:
            size += value

    return size
