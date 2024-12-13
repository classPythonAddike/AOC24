with open("input.txt", "r") as f:
    matrix = f.read().split()

print(*matrix, sep="\n")

count = 0

def generate_neighbours(p, matrix):
    for pos in [
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1]),
        (p[0], p[1] + 1),
        (p[0], p[1] - 1),
        (p[0] + 1, p[1] + 1),
        (p[0] - 1, p[1] - 1),
        (p[0] - 1, p[1] + 1),
        (p[0] + 1, p[1] - 1),
    ]:
        if len(matrix) > pos[0] >= 0 and len(matrix[0]) > pos[1] >= 0:
            yield pos

def search(matrix, pos_x, pos_y, word="XMAS", dirn=None):
    count = 0
    
    if not (len(matrix) > pos_x >= 0 and len(matrix[0]) > pos_y >= 0):
        return 0

    if matrix[pos_x][pos_y] == word[0]:
        if len(word) > 1:
            if dirn is None:
                for p in generate_neighbours((pos_x, pos_y), matrix):
                    if search(matrix, p[0], p[1], word[1:], (p[0] - pos_x, p[1] - pos_y)):
                        count += 1
            else:
                return search(matrix, pos_x + dirn[0], pos_y + dirn[1], word[1:], dirn)
        else:
            return True

    return count

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        count += search(matrix, i, j)

print(count)
