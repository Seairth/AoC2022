
def is_correctly_ordered_lists(left, right) -> bool:
    if len(left) == 0:
        return (1 if len(right) > 0 else 0)

    for index in range(len(left)):
        
        if index == len(right):
            return -1

        l_value = left[index]
        r_value = right[index]

        if type(l_value) is int and type(r_value) is int:
            if l_value < r_value:
                return 1

            if l_value > r_value:
                return -1
        else:
            if type(l_value) is not list:
                l_value = [l_value]

            if type(r_value) is not list:
                r_value = [r_value]

            result = is_correctly_ordered_lists(l_value, r_value)

            if result != 0:
                return result

    return (1 if len(left) < len(right) else 0)
