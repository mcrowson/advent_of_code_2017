from aocd import data
import string

def spin(lst, n):
    # Spins group from end to beginning
    return  lst[-n:] + lst[:-n]

def exchange(lst, first, last):
    # swaps the first and last letters index
    lst[last], lst[first] = lst[first], lst[last]
    return lst

def partner(lst, first, last):
    # swaps the two dancers at first and last
    return exchange(lst, lst.index(first), lst.index(last))

moves_raw = data.split(',')
moves = []
dancers = ['a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

for m in moves_raw:
    op = m[0]
    if op == 's':
        inst = int(m[1:])
    elif op == 'x':
        inst = [int(i) for i in m[1:].split('/')]
    else:
        inst = m[1:].split('/')

    moves.append(
        {
            'operation': op,
            'instructions': inst
        }
    )

dancers = ['a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def dance(dancers, moves):
    for m in moves:
        if m['operation'] == 's':
            dancers = spin(dancers, m['instructions'])
        elif m['operation'] == 'x':
            dancers = exchange(dancers, m['instructions'][0], m['instructions'][1])
        else:
            dancers = partner(dancers, m['instructions'][0], m['instructions'][1])
    return dancers

p1 = dance(dancers, moves)
print('P1: ', ''.join(p1))

count_d = ['a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
hashes = []
counter = 0
while True:
    count_d = dance(count_d, moves)
    h = hash(tuple(count_d))
    if h in hashes:
        break
    hashes.append(h)
    counter += 1

print("Cycle repeats after {} dances. No need to count to 1B".format(counter))
desired_iters = 1000000000
needed_dances = desired_iters % counter

p2 = ['a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
for i in range(needed_dances):
    p2 = dance(p2, moves)

print('P2 ', ''.join(p2))
