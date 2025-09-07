with open("input.txt") as f:
    inp = f.read().strip()

files = list(map(int, inp))

# Index
left_pointer = 0
true_pointer = 0
# Index, Count
right_pointer = len(files) - 1 if len(files) % 2 else len(files) - 2, 0

checksum = 0

while True:
    for i in range(files[left_pointer]):
        checksum += left_pointer // 2 * true_pointer
        true_pointer += 1

    while true_pointer:
        pass
