from aocd import data
import re

no_exclaim = re.sub(r"(!.)", "", data)
no_garbage = re.sub(r"(\<.*?\>)", "", no_exclaim)

total_score = 0
level = 0

for character in no_exclaim:
    if character == '{':
        level += 1
        total_score += level
    elif character == '}':
        level -= 1

print("P1. The garbage score is {}".format(total_score))

garbage_count = 0
for s in re.finditer(r"(\<(.*?)\>)", no_exclaim):
    garbage_count += len(s.group(2))


print("P2. Characters removed {}".format(garbage_count))
