with open("input.txt") as f:
    data = f.read()

r, updates = data.split("\n\n")

rules = {int(i.split("|")[0]): [] for i in r.strip().split("\n")}
for rule in r.strip().split("\n"):
    rules[int(rule.split("|")[0])] += [int(rule.split("|")[1])]

updates = [list(map(int, i.split(","))) for i in updates.strip().split("\n")]
updates = [dict(zip(i, range(len(i)))) for i in updates]

print(rules, *updates, sep="\n")
print("-" * 50)

valid = 0
for update in updates:
    invalid = False
    for page in update:
        for required_page in rules.get(page, []):
            if update.get(required_page, update[page]) < update[page]:
                invalid = True
                break
        if invalid:
            break
    else:
        l = list(sorted(update, key=update.get))
        valid += l[len(l) // 2]

print(valid)
