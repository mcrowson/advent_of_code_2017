import math


def steps(n):
    """The squares expand at squares of odd numbers"""
    sqrt_of_n = math.sqrt(n)
    print(sqrt_of_n)

    lower = int(math.floor(sqrt_of_n))
    if lower % 2 == 0:
        # The number is even, rows start at odd numbers
        lower -= 1

    upper = lower + 2
    outter_row = range(lower**2 + 1, upper**2 + 1)

    max_steps = upper - 1
    min_steps = upper - len(outter_row)/8 - 1
    print("Min {} and max {}".format(min_steps, max_steps))

    current_steps = max_steps
    direction = "down"
    for possible in outter_row[:: -1]:
        # Start at the max number and walk backwards
        if n == possible:
            return current_steps
        if current_steps == max_steps:
            direction = 'down'
        elif current_steps == min_steps:
            direction = 'up'
        if direction == 'down':
            current_steps -= 1
        else:
            current_steps += 1

print("Steps to 1: {}".format(steps(277678)))



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

print("P2 Next Largest Node: {}".format(next_largest_node(target)))
