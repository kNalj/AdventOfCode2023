with open("day03", "r") as f:
    lines = [line.strip() for line in f.readlines()]


nums = []
num = 0
for i, line in enumerate(lines):
    if num != 0:
        nums[-1].append(j - 1)
        nums[-1].append(num)
        num = 0
    num = 0
    for j, char in enumerate(line):
        if char.isdigit():
            if num == 0:
                nums.append([i, j])
            num *= 10
            num += int(char)
        else:
            if num != 0:
                nums[-1].append(j-1)
                nums[-1].append(num)
                num = 0
gears = {}
total = 0
for num in nums:
    valid = False
    for i in range(max(num[0]-1, 0), min(len(lines), num[0] + 2)):
        for j in range(max(0, num[1] - 1), min(len(lines[0]), num[2] + 2)):
            if ((i != num[0]) or (j not in range(num[1], num[2] + 1))) and (lines[i][j] != "." and not lines[i][j].isdigit()):
                if lines[i][j] == "*":
                    if (i, j) not in gears:
                        gears[(i, j)] = [num[3]]
                    else:
                        gears[(i, j)].append(num[3])
                valid = True
            if valid:
                continue
    if valid:
        total += num[3]
        continue

print(total)

gear_ratio = 0
for gear, values in gears.items():
    if len(values) == 2:
        tot = 1
        for val in values:
            tot *= val
        gear_ratio += tot

print(gear_ratio)