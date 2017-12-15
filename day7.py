from aocd import get_data
data = get_data(day=7, year=2017)

program_lines = data.split('\n')

programs = []

# Create dict of programs and details
program_details = {}
for line in program_lines:
    name, weight_children = line.split(' ', 1)
    if ' ' in weight_children:
        weight_raw, children_raw = weight_children.split(' ', 1)
        weight = int(weight_raw.strip('(').strip().strip(')'))
        children = [c.strip() for c in children_raw.strip('->').split(',')]
    else:
        weight = int(weight_children.strip().strip('(').strip(')'))
        children = None

    program_details[name]= {
        'weight': weight,
        'children': children
    }

# Assign the parents
for name, details in program_details.items():
    if details['children']:
        for child in details['children']:
            program_details[child]['parent'] = name

# Find the program without a parent
bottom = [name for name, d in program_details.items() if 'parent' not in d].pop()
print("P1. Program Without a parent: {}".format(bottom))





# Find the cumulative burdens
def cum_burden(program_name):
    # assigns the total weights of a program and its children
    children = program_details[program_name]['children'] or []
    self_weight = program_details[program_name]['weight']
    kid_weights = []

    for c in children:
        if 'burden' not in program_details[c]:
            program_details[c]['burden'] = cum_burden(c)
        kid_weights.append(program_details[c]['burden'])
    program_details[program_name]['children_weights'] = kid_weights
    program_details[program_name]['even_children'] = len(set(kid_weights)) in [0, 1]

    burden = self_weight + sum(kid_weights)
    program_details[program_name]['burden'] = burden
    return burden

program_details[bottom]['burden'] = cum_burden(bottom)

# Get the highest program in the stack
lightest_name = None
lightest = None
for name, details in program_details.items():
    if not details['even_children']:
        if not lightest:
            lightest = details
            lightest_name = name
        elif lightest['burden'] > details['burden']:
            lightest = details
            lightest_name = name


# Find child whose weight doesn't match
possible_w = set(program_details[lightest_name]['children_weights'])
weight_counts = {
    w: program_details[lightest_name]['children_weights'].count(w) for w in possible_w
}
odd_man = None
  for burden, cnt in weight_counts.items()
    if not odd_man:
        odd_man = w
    elif odd_man
program_details[lightest_name]['children'].index(min())

# Subtract six


print(weight_counts
