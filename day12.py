from aocd import data

def get_child_nodes(node_name, children=[]):
    if not children:
        children = [node_name]  # Gets self
    node_kids = pipe_map[node_name]
    new_kids = [n for n in node_kids if n not in children]
    if new_kids:
        children += new_kids
        for n in new_kids:
            children += get_child_nodes(n, children)

    return list(set(children))  # Dedupe if multiple paths brought in same nodes

# Get data and put in dict
pipes = data.split('\n')
pipe_map = {}
for p in pipes:
    l, r = p.split(' <-> ', 1)
    pipe_map[l] = [n.strip() for n in r.split(',')]

print("P1: {}".format(len(get_child_nodes('0'))))

groups = 0
grouped_noded = []

for k in pipe_map.keys():
    if k not in grouped_noded:
        groups += 1
        children = get_child_nodes(k)
        in_a_group += children

print("P2: {}".format(groups))
