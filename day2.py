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

print(total)
