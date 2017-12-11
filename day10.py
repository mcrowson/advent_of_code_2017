from aocd import data

instructions = [int(i) for i in data.split(',')]
input_lst = list(range(256))

current_index = 0
skip = 0

for inst in instructions:
    firstp = input_lst[:current_index]

    end_flip_idx = current_index + inst
    if end_flip_idx > len(input_lst):

        # Wrap around to the beginning
        wrap_len = end_flip_idx - len(input_lst)
        ending = input_lst[current_index:]
        beginning = input_lst[:wrap_len]
        unchanged_middle = input_lst[wrap_len:current_index]

        to_flip = ending + beginning
        flipped = to_flip[::-1]

        ending_flipped = flipped[:len(ending)]
        beginning_flipped = flipped[len(ending):]

        reconst = beginning_flipped + unchanged_middle + ending_flipped

    else:
        # All in a line
        flipped = input_lst[current_index:current_index + inst][::-1]
        reconst = input_lst[:current_index] + flipped + input_lst[current_index + inst:]


    input_lst = reconst
    current_index = (current_index + skip + inst) % len(input_lst)
    skip += 1

print("P1: {}".format(input_lst[0] * input_lst[1]))


p2_input_lst = list(range(255))
ascii_inst = [ord(s) for s in data] + [17, 31, 73, 47, 23]

current_index = 0
skip = 0

for rnd in range(64):
    for inst in ascii_inst:
        firstp = p2_input_lst[:current_index]

        end_flip_idx = current_index + inst
        if end_flip_idx > len(p2_input_lst):

            # Wrap around to the beginning
            wrap_len = end_flip_idx - len(p2_input_lst)
            ending = p2_input_lst[current_index:]
            beginning = p2_input_lst[:wrap_len]
            unchanged_middle = p2_input_lst[wrap_len:current_index]

            to_flip = ending + beginning
            flipped = to_flip[::-1]

            ending_flipped = flipped[:len(ending)]
            beginning_flipped = flipped[len(ending):]

            reconst = beginning_flipped + unchanged_middle + ending_flipped

        else:
            # All in a line
            flipped = p2_input_lst[current_index:current_index + inst][::-1]
            reconst = p2_input_lst[:current_index] + flipped + p2_input_lst[current_index + inst:]


        p2_input_lst = reconst
        current_index = (current_index + skip + inst) % len(p2_input_lst)
        skip += 1

# Make the Hash
dense_hash = []
block_size = len(p2_input_lst) / 16
for block in range(16):
    starting = int(block * block_size)
    ending = int(block * block_size + block_size)
    dense_hash_block = int(p2_input_lst[starting])
    for i in range(int(block_size - 1)):
        if p2_input_lst[i+1] == ',':
            continue
        dense_hash_block ^= int(p2_input_lst[i+1])
    print(dense_hash_block)
    dense_hash.append(dense_hash_block)

print(dense_hash)
#hexed
hexed = ''.join([hex(h)[2:] for h in dense_hash])
print(hexed)
