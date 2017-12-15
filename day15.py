

def gen(previous, constant, mult):
    new_v = (constant * previous) % 2147483647
    if new_v % mult == 0:
        yield new_v
    previous = new_v
    while True:
        new_v = (constant * previous) % 2147483647
        if new_v % mult == 0:
            yield new_v
        previous = new_v

def count_matching_pairs(st_a, st_b, loop_count, mult_a=1, mult_b=1):
    # Counts the matching pairs from generators given two starting points
    a_const = 16807
    b_const = 48271

    matching = 0
    for i, r_tuple in enumerate(zip(gen(st_a, a_const, mult_a), gen(st_b, b_const, mult_b))):
        a = "{0:b}".format(r_tuple[0])[-16:]
        b = "{0:b}".format(r_tuple[1])[-16:]
        if a == b:
            matching += 1

        if i == loop_count - 1:  # Less one for index 0
            break
    return matching

example_res = count_matching_pairs(65, 8921, 5)
assert(1 == example_res)

p1_res = count_matching_pairs(116, 299, 40000000)
print("P1: {}".format(p1_res))

example2_res = count_matching_pairs(
    st_a=65,
    st_b=8921,
    loop_count=5000000,
    mult_a=4,
    mult_b=8)
assert(309 == example2_res)

p2_res = count_matching_pairs(
    st_a=116,
    st_b=299,
    loop_count=5000000,
    mult_a=4,
    mult_b=8)
print("P2: {}".format(p2_res))
