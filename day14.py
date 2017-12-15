from day10 import knot_to_inst, sparse_hash

def hex2bits(inp):
    return ''.join(["{0:04b}".format(int(i, base=16)) for i in inp])

def compute_row(row_key):
    ascii_key = [ord(s) for s in row_key] + [17, 31, 73, 47, 23]
    key_hash = sparse_hash(knot_to_inst(ascii_key, deep=64))
    bits = hex2bits(key_hash)
    return bits

def compute_grid(key):
    bits = []
    for row_index in range(128):
        bits.append(compute_row('{}-{}'.format(key, row_index)))
    return bits

# Confirm the example
ex_grid = compute_grid('flqrgnkx')
assert(8108 == sum([row.count('1') for row in ex_grid]))

pgrid = compute_grid('vbqugkhl')
print("P1: {}".format(sum([row.count('1') for row in pgrid])))



def find_touching(x, y, grid, seen=None):
    # Given an (x,y) position in grid, find those nodes touching it
    if grid[x][y] == 0:
        # There is nothing here
        return []

    if not seen:
        seen = []
    seen.append((x, y))


    print("Found a 1 in point {} {}. It is not in {}".format(x, y, seen))
    # Add self to touching list
    touching = [(x, y)]

    # Identify adjacents we have not seen
    adj = []
    if x != 0 and (x - 1, y) not in seen:
        adj.append((x - 1, y))
    if x != 127 and (x + 1, y) not in seen:
        adj.append((x + 1, y))
    if y != 0 and (x, y - 1) not in seen:
        adj.append((x, y - 1))
    if y != 127 and (x, y + 1) not in seen:
        adj.append((x, y + 1))

    # and add their results to this list, return this list
    for a in adj:
        touching += find_touching(a[0], a[1], grid, seen)

    return list(set(touching))

print(find_touching(0, 0, ex_grid))
#print(ex_grid[0][0])

grouped = []
