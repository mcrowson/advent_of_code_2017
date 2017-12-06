with open('day2.txt') as f:
    lines = f.readlines()

lns = []
for line in lines:
    nums = [int(n) for n in line.split()]
    lns.append(nums)

total = 0

for line in lns:
    for n in line:
        for m in line:
            if n == m:
                continue
            if n % m == 0:
                total += n/m

print(total)


def loop_test(line):
    candidates = []


    ln_len = len(lines)
    for x in range(ln_len):
        for i in range(ln_len):
            if x + i < ln_len:
                if line[x] % line[x + i] == 0 or line[x + i] % line[x] == 0:
                    candidates = [line[x], line[x + i]]
    if len(candidates) > 0:
        print(candidates)
        res = int(max(candidates) / min(candidates))
        print("Got something {}".format(res))
        return res
    else:
        return 0

jar = sum([loop_test(l) for l in lns])
print(jar)
