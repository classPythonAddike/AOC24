arr_1 = []
arr_2 = []

with open("input.txt", "r") as f:
	for line in f:
		arr_1 += [int(line.strip().split()[0])]
		arr_2 += [int(line.strip().split()[-1])]

print(sum(map(lambda el: arr_2.count(el) * el, arr_1)))