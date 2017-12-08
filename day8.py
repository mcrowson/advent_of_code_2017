with open('day8_input.txt') as f:
    operations = f.readlines()

registers = {}

highest_val = 0
# Populate the registers
for op in operations:
    name, direc, val, ifs, dep, oper, dep_val = op.split(' ')
    # Put registers in if they don't exist
    if name not in registers:
        registers[name] = 0
    if dep not in registers:
        registers[dep] = 0

    # Check the condition
    if eval('{} {} {}'.format(registers[dep], oper, dep_val)):
        mod = 1 if direc == 'inc' else -1
        inc = mod * int(val)
        registers[name] += inc

        if registers[name] > highest_val:
            highest_val = registers[name] 


print("P1. Max Value in any register is {}".format(max(registers.values())))
print("P2. Max value in any register during the program is {}".format(highest_val))
