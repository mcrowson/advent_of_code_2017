with open('day_5_input.txt') as f:
    lines = [int(l) for l in f.readlines()]


steps = 0
list_position = 0
list_len = len(lines)
while True:
    if list_position >= list_len:
        print("Exited the list in {} steps".format(steps))
        break
    next_loc = list_position + lines[list_position]  # Get next next index
    if lines[list_position] >= 3:
        lines[list_position] -= 1
    else:
        lines[list_position] += 1  # Increment current index
    list_position = next_loc
    steps += 1
