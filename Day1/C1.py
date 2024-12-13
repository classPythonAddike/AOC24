arr_1 = []
arr_2 = []

with open("input.txt", "r") as f:
	for line in f:
		arr_1 += [int(line.strip().split()[0])]
		arr_2 += [int(line.strip().split()[-1])]

arr_1.sort()
arr_2.sort()

print(sum(map(lambda tup: abs(tup[0] - tup[1]), zip(arr_1, arr_2))))