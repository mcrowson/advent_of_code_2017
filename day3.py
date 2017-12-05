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
