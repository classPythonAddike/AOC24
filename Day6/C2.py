import os
import time
import copy

clear = lambda: os.system("clear")

with open("input.txt") as f:
    inp = f.read().strip().split("\n")

# North: 1000
# East : 0100
# South: 0010
# West : 0001

NORTH = 0b1000
EAST  = 0b0100
SOUTH = 0b0010
WEST  = 0b0001

visitable = {
    (i, j): NORTH if inp[i][j] == "^" else 0 for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] != "#"
}

blocks = {
    (i, j) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == "#"
}

pos = [t for t in visitable if visitable[t] == NORTH][0]
start_pos = pos
dirn = NORTH


def format(visitable, blocks, pos=None, cls=False):
    if cls: clear()

    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if pos == (i, j):
                print("O", end="")
            elif (i, j) == start_pos:
                print("^", end="")
            elif visitable.get((i, j)) is not None:
                print([".", "X"][bool(visitable[(i, j)])], end="")
            else:
                print("#", end="")
        print()


format(visitable, blocks)
print(pos, end="\n\n")


def in_grid(pos, inp):
    return len(inp) > pos[0] >= 0 and len(inp[0]) > pos[1] >= 0


def dirn_in(dirn, pos, visitable):
    return bool(dirn & visitable.get(pos, 0))


def write_dirn(dirn, pos, visitable):
    return dirn | visitable.get(pos, 0)


def right_turn(dirn):
    return ((dirn + (dirn << 4)) >> 1) & 0b1111


def forward(pos, dirn):
    match dirn:
        case 0b1000:
            return (pos[0] - 1, pos[1])
        case 0b0100:
            return (pos[0], pos[1] + 1)
        case 0b0010:
            return (pos[0] + 1, pos[1])
        case 0b0001:
            return (pos[0], pos[1] - 1)
        case _:
            raise Exception(f"Invalid direction!: {bin(dirn)}, Pos: {pos}")


def move(pos, dirn, blocks):
    next_pos = forward(pos, dirn)

    if not next_pos in blocks:
        return next_pos, dirn

    return pos, right_turn(dirn)


def loop_possible(pos, block_pos, dirn, blocks):
    if block_pos in blocks or not in_grid(block_pos, inp) or block_pos == start_pos:
        return False

    blocks.add(block_pos)
    
    visited = {}

    while True:
        pos, dirn = move(pos, dirn, blocks)

        if not in_grid(pos, inp):
            blocks.remove(block_pos)
            return False

        if dirn_in(dirn, pos, visited):
            blocks.remove(block_pos)
            return True
        
        visited[pos] = write_dirn(dirn, pos, visited)


count = 0
loop_blocks = set()
while True:
    next_pos, dirn = move(pos, dirn, blocks)
    
    if not in_grid(next_pos, inp):
        break

    if next_pos not in loop_blocks and loop_possible(start_pos, next_pos, NORTH, blocks):
        loop_blocks.add(next_pos)
        count += 1
    
    pos = next_pos
    visitable[pos] = write_dirn(dirn, pos, visitable)


print()
print(count)
