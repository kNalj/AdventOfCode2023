with open("day14", "r") as f:
    lines = [[i for i in line.strip()] for line in f.readlines()]


def plines(lines):
    for line in lines:
        print(line)
    print()


def roll_north(rock_map):
    destinations = [0 for _ in range(len(rock_map[0]))]
    for i, line in enumerate(rock_map):
        for j, col in enumerate(line):
            if rock_map[i][j] == "O":
                rock_map[i][j] = "."
                rock_map[destinations[j]][j] = "O"
                destinations[j] += 1
            elif rock_map[i][j] == "#":
                destinations[j] = i+1


def roll_south(rock_map):
    destinations = [len(rock_map)-1 for _ in range(len(rock_map[0]))]
    for i, line in enumerate(rock_map):
        for j, col in enumerate(line):
            if rock_map[len(rock_map) - (i + 1)][j] == "O":
                rock_map[len(rock_map) - (i + 1)][j] = "."
                rock_map[destinations[j]][j] = "O"
                destinations[j] -= 1
            elif rock_map[len(rock_map) - (i + 1)][j] == "#":
                destinations[j] = (len(rock_map) - (i + 1)) - 1


def roll_east(rock_map):
    destinations = [len(rock_map) - 1 for _ in range(len(rock_map))]
    for i in range(len(rock_map[0])):
        for j, row in enumerate(rock_map):
            if rock_map[j][len(rock_map[0]) - (i + 1)] == "O":
                rock_map[j][len(rock_map[0]) - (i + 1)] = "."
                rock_map[j][destinations[j]] = "O"
                destinations[j] -= 1
            elif rock_map[j][len(rock_map[0]) - (i + 1)] == "#":
                destinations[j] = (len(rock_map) - (i + 1)) - 1


def roll_west(rock_map):
    destinations = [0 for _ in range(len(rock_map))]
    for i in range(len(rock_map[0])):
        for j, row in enumerate(rock_map):
            if rock_map[j][i] == "O":
                rock_map[j][i] = "."
                rock_map[j][destinations[j]] = "O"
                destinations[j] += 1
            elif rock_map[j][i] == "#":
                destinations[j] = i + 1


counter = 0
repeat_counter = 0
previous = []
for i in range(1000000000):
    roll_north(lines)
    roll_west(lines)
    roll_south(lines)
    roll_east(lines)
    if lines in previous:
        repeat_counter += 1
        if repeat_counter == 4:
            break
    previous.append([[i for i in line] for line in lines])
    counter += 1


print(counter)
print(repeat_counter)

print(1000000000 % (counter - repeat_counter))

# roll_north(lines)
# plines(lines)
sum = 0
for i, line in enumerate(lines):
    for j in line:
        if j == "O":
            sum += (len(lines) - i)

print(sum)