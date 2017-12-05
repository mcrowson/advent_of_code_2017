
def adjacent_cells(x , y):
    # Gets a list of adjacent cells
    adjacents = list()
    for xv in [x-1, x, x+1]:
        for yv in [y-1, y, y+1]:
            if xv == x and yv == y:
                continue
            adjacents.append((xv, yv))
    return adjacents

def next_largest_node(target):
    # Gets the node with the next largest value from target
    spiral = {}  # Hashmap of locations and values
    step_len = 1  # Initial length
    current_node = (0, 0)  # Start from center of cartecian plane
    spiral[current_node] = 1  # initial value

    while True:
        if step_len % 2 == 1:
            step_mod = 1  # Odd num steps, increase x/y
        else:
            step_mod = -1  # Even num steps decrease x/y

        # Walk X
        for axis in ['x', 'y']:
            for s in range(1, step_len + 1):
                if axis == 'x':
                    current_node = tuple([current_node[0] + (1 * step_mod), current_node[1]])
                else:
                    current_node = tuple([current_node[0], current_node[1] + (1 * step_mod)])
                adj = adjacent_cells(*current_node)
                spiral[current_node] = sum([spiral[a] for a in adj if a in spiral])

                if spiral[current_node] > target:
                    return(spiral[current_node])

        step_len += 1


target = 277678

print(next_largest_node(target))
