with open("example", "r") as f:
    lines = [[i for i in line.strip()] for line in f.readlines()]


mvs = {
    "r": [1, 0],
    "d": [0, 1],
    "l": [-1, 0],
    "u": [0, -1]
}


def get_next_sign(map, x, y):
    if (x > len(map[0]) - 1) or (y > len(map)):
        return None
    else:
        return map[x][y]


def handle_beam()


def make_move(map, levels, beams, beam_index):
    beam = beams[beam_index]
    start_y, start_x = beam[0]
    dx, dy = mvs[beam[1]]
    end_x, end_y = start_x+dx, start_y+dy
    print(f"Moving [{start_x}, {start_y}] -> [{end_x}, {end_y}]")
    next_sign = get_next_sign(map, end_x, end_y)
    if next_sign is None:
        del beams[beam_index]
    else:
        handle_beam(map, )


for line in lines:
    print(line)

visited = [[0 for i in line] for line in lines]

for line in visited:
    print(line)

beams = [[(0, 0), "r"]]
while beams:
    for i in range(len(beams)):
        make_move(lines, visited, beams, i)