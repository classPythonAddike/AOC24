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

reordered = []
for update in updates:
    wrong_order = False
    for page in update:
        for required_page in rules.get(page, []):
            if update.get(required_page, update[page]) < update[page]:
                wrong_order = True
                break
    
        if wrong_order:
            reordered.append(update)
            break

print(*reordered, sep="\n")
print("-" * 50)

def make_swaps(rules, update):
    for page in update:
        for required_page in rules.get(page, []):
            if update.get(required_page, update[page]) < update[page]:
                update[page], update[required_page] = update[required_page], update[page]
                return update, True
    return update, False


tot_sum = 0
for update in reordered:
    new_update, swapped = make_swaps(rules, update)
    
    while swapped:
        new_update, swapped = make_swaps(rules, update)

    tot_sum += [j for j in new_update if new_update[j] == len(new_update) // 2][0]

print(tot_sum)
