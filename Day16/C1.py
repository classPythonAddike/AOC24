from enum import Enum

class DIRN(Enum):
    NORTH = 0b1000
    EAST  = 0b0100
    SOUTH = 0b0010
    WEST  = 0b0001

FORW_PEN = 1
TURN_PEN = 1000

class Deer():
    def __init__(self, start_pos, start_score=0, start_dir=DIRN.EAST):
        self.start_pos = start_pos
        self.start_score = start_score
        self.start_dir = start_dir
        
        self.current_pos = current_pos
        self.current_score = start_score
        self.current_dirn = start_dir

    def right(self):
        return ((self.current_dirn + (self.current_dirn << 4)) >> 1) & 0b1111
    
    def left(self):
        return ((self.current_dirn << 1) + (self.current_dirn >> 3)) & 0b1111

    def compare_loc_score(self, score, dirn):
        if {self.current_dirn, dirn} in [
            {DIRN.NORTH, DIRN.SOUTH},
            {DIRN.EAST, DIRN.WEST}
        ]:
            return self.current_score + 2 * TURN_PEN < score

        return self.current_score + TURN_PEN < score

    def is_move_possible(self, blocks, pos=None, dirn=None):
        if pos is not None: pos = self.current_pos
        if dirn is not None: dirn = self.current_dirn

        next_pos = (-1, -1)

        match dirn:
            case DIRN.NORTH:
                next_pos = (pos[0] - 1, pos[1])
            case DIRN.EAST:
                next_pos = (pos[0], pos[1] + 1)
            case DIRN.SOUTH:
                next_pos = (pos[0] + 1, pos[1])
            case DIRN.WEST:
                next_pos = (pos[0], pos[1] - 1)


    def possible_moves(self, blocks):
        dirns = [
            self.left(),
            self.current_dirn,
            self.right()
        ]

        for dirn in dirns:
            pass

    def move(self, blocks):
        pass

    def clone(self, blocks):
        pass

with open("input.txt", "r") as f:
    inp = f.readlines()

blocks = {
    (i, j) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == "#"
}

start_pos = (0, 0)
end_pos = (0, 0)
dirn = DIRN.EAST

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i][j] == "S":
            start_pos = i, j
        elif inp[i][j] == "E":
            end_pos = i, j


