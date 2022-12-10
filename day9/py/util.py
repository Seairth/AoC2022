
def render_rope(rope):
    min_x = min(min([k[0] for k in rope]), 0)
    max_x = max(max([k[0] for k in rope]), 0)

    min_y = min(min([k[1] for k in rope]), 0)
    max_y = max(max([k[1] for k in rope]), 0)

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if x == 0 and y == 0:
                v = 's'
            else:
                v = '.'

            for k in range(len(rope) - 1, -1, -1):
                if rope[k] == (x, y):
                    v = chr(ord('0') + k)
    
            print(v, end='')

        print('')
    
    print ('')

def update_tail_recursive(head_index, rope, visited):
    head = rope[head_index]
    tail = rope[head_index + 1]

    x_distance = abs(head[0] - tail[0])
    y_distance = abs(head[1] - tail[1])

    if x_distance > 1 or y_distance > 1:
        if head[0] == tail[0]:
            # same col
            if head[1] > tail[1]:
                tail = (tail[0], tail[1]+1)
            else:
                tail = (tail[0], tail[1]-1)

        elif head[1] == tail[1]:
            # same row
            if head[0] > tail[0]:
                tail = (tail[0]+1, tail[1])
            else:
                tail = (tail[0]-1, tail[1])
        else:
            # diagonal
            x_move = head[0] > tail[0] and 1 or -1
            y_move = head[1] > tail[1] and 1 or -1

            tail = (tail[0] + x_move, tail[1] + y_move)

        rope[head_index + 1] = tail

        if head_index + 1 == len(rope) - 1:
            visited.add(tail)
        else:
            update_tail_recursive(head_index + 1, rope, visited)

def simulate_rope(rope_len):
    visited = set()

    rope = []

    for knot in range(0, rope_len):
        rope.append((0,0))

    visited.add(rope[-1])

    with open('../input.txt', 'r') as f:
        for line in f:
            direction = line[0]
            distance = int(line[2:])
            
            # print(f">>> {direction} {distance}")

            for step in range(0, distance):
                head = rope[0]

                if direction == 'U':
                    head = (head[0], head[1]+1)
                elif direction == 'D':
                    head = (head[0], head[1]-1)
                elif direction == 'R':
                    head = (head[0]+1, head[1])
                elif direction == 'L':
                    head = (head[0]-1, head[1])

                rope[0] = head

                update_tail_recursive(0, rope, visited)

                # render_rope(rope)

    return len(visited)
