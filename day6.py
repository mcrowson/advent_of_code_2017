with open('day6_input.txt') as f:
    lines = f.readlines()

BANK_LEVELS = [int(i) for i in lines[0].split()]
BANK_COUNT = len(BANK_LEVELS)
redist_cycles = 0

def distribute_blocks(block_count, starting_bank=None):
    """Takes a number of blocks and possible starting bank position
    and distribute blocks evenly"""
    if not starting_bank:
        starting_bank = 0
    for i in range(starting_bank, BANK_COUNT):
        if block_count > 0:
            BANK_LEVELS[i] += 1
            block_count -= 1
        else:
            return  # No more blocks left to distribute
    # Got to end of bank but have more blocks
    return distribute_blocks(block_count)



bank_level_hashes = {}

while True:
    # Get the hash of the current BANK_LEVELS and see if it has been seen
    bl_hash = hash(tuple(BANK_LEVELS))
    if bl_hash in bank_level_hashes:
        cycles_from_first_seen = redist_cycles - bank_level_hashes[bl_hash]
        print("P1. Found existing configuration in {} cycles".format(redist_cycles))
        print("P2. This took {} cycles between the same bank conf".format(cycles_from_first_seen))
        break
    bank_level_hashes[bl_hash] = redist_cycles  # Cycle number of hash
    redist_cycles += 1


    max_register_value = max(BANK_LEVELS)
    max_register_index = BANK_LEVELS.index(max_register_value)
    BANK_LEVELS[max_register_index] = 0  # Empty current bank
    distribute_blocks(max_register_value, max_register_index + 1)
