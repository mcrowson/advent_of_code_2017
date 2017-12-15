from aocd import get_data
import operator
from functools import reduce
from numpy import array_split

data = get_data(year=2017, day=10)

def knot_to_inst(instructions, input_lst=None, skip=0, current_index=0, deep=1):
    """
    input_lst: The list to be scrabled
    instructions: The scrable in instructions
    skip: Amount to skip indexes between instructions
    current_index: Current index for instruction
    deep: How many times to perform scramble
    """
    if not input_lst:
        input_lst = list(range(256))

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
        return knot_to_inst(instructions, input_lst, skip, current_index, deep)
    return input_lst


def sparse_hash(scrambled):
    # Takes a scrambled knot and makes a hash
    blocked_list = array_split(scrambled, 16)
    dense_hashes = [reduce(operator.xor, c, 0) for c in blocked_list]
    sparse_hash = ''.join([hex(h)[2:].zfill(2) for h in dense_hashes])
    return sparse_hash

if __name__ == "__main__":
    instructions = [int(i) for i in data.split(',')]
    p1 = knot_to_inst(instructions)
    print("P1: {}".format(p1[0] * p1[1]))

    ascii_inst = [ord(s) for s in data]
    salt = [17, 31, 73, 47, 23]
    p2 = knot_to_inst(ascii_inst + salt, deep=64)
    print("P2: {}".format(sparse_hash(p2)))

    inst = [ord(s) for s in 'AoC 2017'] + [17, 31, 73, 47, 23]
    aoc = sparse_hash(knot_to_inst(inst, deep=64))
    assert('33efeb34ea91902bb2f59c9920caa6cd' == aoc)
    print("AoC 2017: {}".format(aoc))
    empty_inst = [17, 31, 73, 47, 23]
    empty = sparse_hash(knot_to_inst(empty_inst, deep=64))
    print("Empty String: {}".format(empty))
    assert('a2582a3a0e66e6e86e3812dcb672a272' == empty)
