from collections import defaultdict
from aocd import data

registers = defaultdict(int)

highest_val = 0
# Populate the registers
for op in data.split('\n'):
    name, direc, val, ifs, dep, oper, dep_val = op.split(' ')

    # Check the condition
    if eval('{} {} {}'.format(registers[dep], oper, dep_val)):
        mod = 1 if direc == 'inc' else -1
        inc = mod * int(val)
        registers[name] += inc

        if registers[name] > highest_val:
            highest_val = registers[name]

print("P1. Max Value in any register is {}".format(max(registers.values())))
print("P2. Max value in any register during the program is {}".format(highest_val))
