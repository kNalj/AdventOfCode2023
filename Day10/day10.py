with open("day10", "r") as f:
    lab = [line.strip() for line in f.readlines()]
for i, line in enumerate(lab):
    for j, letter in enumerate(line):
        if letter == "S":
            start = i, j
node_map = {
    (True, True, False, False): "|", (True, False, True, False): "J", (True, False, False, True): "L",
    (False, True, True, False): "7", (False, True, False, True): "F", (False, False, True, True): "-",
}


def get_start_shape(node, lab):
    up, down, left, right = False, False, False, False
    if lab[node[0]-1][node[1]] in ["|", "7", "F"]:
        up = True
    if lab[node[0] + 1][node[1]] in ["|", "J", "L"]:
        down = True
    if lab[node[0]][node[1]+1] in ["7", "-", "J"]:
        right = True
    if lab[node[0]][node[1]-1] in ["-", "L", "F"]:
        left = True

    return node_map[(up, down, left, right)]


lab[start[0]] = lab[start[0]][:start[1]] + get_start_shape((start[0], start[1]), lab) + lab[start[0]][start[1]+1:]


def get_neighbors(node, lab, distances):
    x, y = node
    if lab[x][y] == "|":
        mods = [[-1, 0], [1, 0]]
    elif lab[x][y] == "-":
        mods = [[0, -1], [0, 1]]
    elif lab[x][y] == "F":
        mods = [[1, 0], [0, 1]]
    elif lab[x][y] == "J":
        mods = [[-1, 0], [0, -1]]
    elif lab[x][y] == "7":
        mods = [[1, 0], [0, -1]]
    elif lab[x][y] == "L":
        mods = [[-1, 0], [0, 1]]

    return [(x+mod[0], y+mod[1]) for mod in mods if distances[x+mod[0]][y+mod[1]] is None]


distances = [[None for item in i] for i in lab]
distances[start[0]][start[1]] = 0

nodes = [start]
while nodes:
    new_neighbors = []
    for node in nodes:
        new_neighbors += get_neighbors(node, lab, distances)
        for n in new_neighbors:
            distances[n[0]][n[1]] = distances[node[0]][node[1]] + 1 if distances[n[0]][n[1]] is None else min(distances[node[0]][node[1]] + 1, distances[n[0]][n[1]])
    nodes = new_neighbors

max = 0
for line in distances:
    for i in line:
        if i is not None and i > max:
            max = i

print(max)