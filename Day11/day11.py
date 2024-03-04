with open("day11", "r") as f:
    universe = [line.strip() for line in f.readlines()]

rows = []
for i, line in enumerate(universe):
    expands = True
    for space in line:
        if space != ".":
            expands = False
            break
    if expands:
        rows.append(i)


columns = []
for i in range(len(universe[0])):
    full_column = [line[i] for line in universe]
    expands = True
    for space in full_column:
        if space != ".":
            expands = False
            break
    if expands:
        columns.append(i)


galaxies = []
for i, line in enumerate(universe):
    for j, space in enumerate(line):
        if universe[i][j] == "#":
            galaxies.append([i, j])


def calc_distance(a, b, duplication_factor):
    row_range = min(a[0], b[0]), max(a[0], b[0])
    column_range = min(a[1], b[1]), max(a[1], b[1])
    rows_between = [row for row in rows if row > row_range[0] and row < row_range[1]]
    columns_between = [column for column in columns if column > column_range[0] and column < column_range[1]]
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + (len(rows_between) + len(columns_between)) * duplication_factor


distance = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        distance += calc_distance(galaxies[i], galaxies[j], 1)
print(distance)

distance = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        distance += calc_distance(galaxies[i], galaxies[j], 999999)
print(distance)