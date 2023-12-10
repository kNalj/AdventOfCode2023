def get_next_stage(line):
    next_stage = []
    for a in range(1, len(line)):
        next_stage.append(line[a] - line[a-1])
    return next_stage


with open("day09", "r") as f:
    lines = [[int(num) for num in line.strip().split(" ")] for line in f.readlines()]

solutions = []
for line in lines:
    solutions.append([line])
    current = line
    while any(current):
        current = get_next_stage(current)
        solutions[-1].append(current)

print(solutions)
for group in solutions:
    group[-1].append(0)
    group[-1] = [0] + group[-1]
    for hist in range(len(group)-1, 0, -1):
        group[hist-1].append(group[hist-1][-1] + group[hist][-1])
        group[hist-1] = [group[hist-1][0]-group[hist][0]] + group[hist-1]
print(solutions)

print(sum([grp[0][-1] for grp in solutions]))
print(sum([grp[0][0] for grp in solutions]))