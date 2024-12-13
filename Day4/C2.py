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

def search(matrix, pos_x, pos_y, word="MAS", dirn=None):
    count = []
    
    if not (len(matrix) > pos_x >= 0 and len(matrix[0]) > pos_y >= 0):
        return 0

    if matrix[pos_x][pos_y] == word[0]:
        if len(word) > 1:
            if dirn is None:
                for p in generate_neighbours((pos_x, pos_y), matrix):
                    if search(matrix, p[0], p[1], word[1:], (p[0] - pos_x, p[1] - pos_y)):
                        count += [(p[0] - pos_x, p[1] - pos_y)]
            else:
                return search(matrix, pos_x + dirn[0], pos_y + dirn[1], word[1:], dirn)
        else:
            return True

    return count

results = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        c = search(matrix, i, j)
        if c:
            results[(i, j)] = [k for k in c if k[0] and k[1]]

print(results)

def x_dirns(matrix, pos, dirn):
    possible = [
        (
            (pos[0] + 2 * dirn[0], pos[1]),
            (dirn[0] * -1, dirn[1])
        ),
        (
            (pos[0], pos[1] + 2 * dirn[1]),
            (dirn[0], dirn[1] * -1)
        ),
    ]

    for pos_new, dirn_new in possible:
        if len(matrix) > pos_new[0] >= 0 and len(matrix[0]) > pos_new[1] >= 0:
            yield pos_new, dirn_new

count = 0
for pos in results:
    for dir in results[pos]:
        for x_pos, x_dir in x_dirns(matrix, pos, dir):
            if x_dir in results.get(x_pos, []):
                count += 1

print(count // 2)
