import os

clear = lambda: os.system('clear')

with open("input.txt") as f:
    inp = f.read().strip().split("\n")

def transform(char):
    return {
        ".": (True, False),
        "#": (False, False),
        "^": (True, True)
    }[char]

grid = {
    (i, j): transform(inp[i][j]) for i in range(len(inp)) for j in range(len(inp[i]))
}

print(*inp, sep="\n")

pos = [(i, j) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == "^"][0]

print(pos)

dirn = (-1, 0)

def format(grid):
    clear()
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            info = grid[(i, j)]
            print({(True, False): ".", (True, True): "X", (False, False): "#"}[info], end="")
        print()

def in_grid(pos, inp):
    return len(inp) > pos[0] >= 0 and len(inp[0]) > pos[1] >= 0

def right_turn(dirn):
    return dirn[1], -dirn[0]

while in_grid(pos, inp):
    while not grid[pos][0]:
        pos = (pos[0] - dirn[0], pos[1] - dirn[1])
        dirn = right_turn(dirn)
        pos = (pos[0] + dirn[0], pos[1] + dirn[1])

    grid[pos] = (True, True)
    pos = (pos[0] + dirn[0], pos[1] + dirn[1])

print(sum([1 for key in grid if grid[key] == (True, True)]))
