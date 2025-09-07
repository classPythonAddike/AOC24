import itertools

with open("input.txt") as f:
    inp = f.read().strip().split("\n")

height = len(inp)
width = len(inp[0])

node_map = {
    (i, j): 0 for i in range(height) for j in range(width)
}

antennas = {}

for i in range(height):
    for j in range(width):
        if inp[i][j] == ".":
            continue

        antennas[inp[i][j]] = antennas.get(inp[i][j], []) + [(i, j)]

print(f"Number of antennas: {sum(map(len, antennas.values()))}")

def format(node_blocks):
    for i in range(height):
        for j in range(width):
            if (i, j) in sum(antennas.values(), []):
                print("A", end="")
            else:
                print(".#"[node_blocks[(i, j)]], end="")
        print()

def in_grid(pos):
    return height > pos[0] >= 0 and width > pos[1] >= 0

def subtract(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]

def add(c1, dirn):
    return c1[0] + dirn[0], c1[1] + dirn[1]

for antenna_freq, antenna_coords in antennas.items():
    for c1, c2 in itertools.combinations(antenna_coords, 2):
        dirn = subtract(c1, c2)

        node_pos = add(c1, dirn)
        
        if in_grid(node_pos):
            node_map[node_pos] = True

        node_pos = subtract(c2, dirn)

        if in_grid(node_pos):
            node_map[node_pos] = True

format(node_map)
print(sum(node_map.values()))
