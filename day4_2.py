
with open('day4_passphrases.txt') as f:
    lines = f.readlines()


valid = 0
for line in lines:
    words = [''.join(sorted(w)) for w in line.split()]  # Lines into list of words. Words are sorted lists of letters
    counts = {w:0 for w in words}  # Dict of words and counts
    for w in counts.keys():
        counts[w] = words.count(w)  # Update the dict
    if not all([v == 1 for v in counts.values()]):
        # Invalid phrase
        continue
    valid += 1

print(valid)
