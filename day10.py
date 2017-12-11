from aocd import data
import operator
from functools import reduce
from numpy import array_split

def scrable_to_instructions(input_lst, instructions, skip=0, current_index=0, deep=1):
    """
    input_lst: The list to be scrabled
    instructions: The scrable in instructions
    skip: Amount to skip indexes between instructions
    current_index: Current index for instruction
    deep: How many times to perform scramble
    """
    for inst in instructions:
        firstp = input_lst[:current_index]

        end_flip_idx = current_index + inst
        if end_flip_idx > len(input_lst):

            # Wrap around to the beginning
            wrap_len = end_flip_idx - len(input_lst)
            ending = input_lst[current_index:]
            beginning = input_lst[:wrap_len]

            to_flip = ending + beginning
            flipped = to_flip[::-1]

            reconst = flipped[len(ending):] + input_lst[wrap_len:current_index] + flipped[:len(ending)]

        else:
            # All in a line
            flipped = input_lst[current_index:current_index + inst][::-1]
            reconst = input_lst[:current_index] + flipped + input_lst[current_index + inst:]

        input_lst = reconst
        current_index = (current_index + skip + inst) % len(input_lst)
        skip += 1
    deep -= 1
    if deep:
        return scrable_to_instructions(input_lst, instructions, skip, current_index, deep)
    return input_lst


instructions = [int(i) for i in data.split(',')]
input_lst = list(range(256))

p1 = scrable_to_instructions(input_lst, instructions)
print("P1: {}".format(p1[0] * p1[1]))


ascii_inst = [ord(s) for s in data] + [17, 31, 73, 47, 23]
p2 = scrable_to_instructions(input_lst, ascii_inst, deep=64)

# Make the Hash
dense_hash = []
blocked_list = array_split(p2, 16)
dense_hashes = [reduce(operator.xor, c, 0) for c in blocked_list]
sparse_hash = ''.join([hex(h)[2:].zfill(2) for h in dense_hashes])
print("P2: {}".format(sparse_hash))
