import re

regex = re.compile(r"(mul\(\d\d?\d?,\d\d?\d?\))|(do\(\))|(don't\(\))")

with open("input.txt") as f:
    inp = f.read().strip()

raw_results = regex.findall(inp)
print(raw_results)
results = []

doing = True
for i in raw_results:
    if i[1]:
        doing = True
    elif i[2]:
        doing = False
    elif doing:
        print(i[0])
        results.append(i[0])

results = [tuple(map(int, i[4:-1].split(","))) for i in results]
print(sum([i*j for i, j in results]))
