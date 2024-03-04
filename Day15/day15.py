with open("day15", "r") as f:
    inputs = f.readline().split(",")


def get_value(code):
    cv = 0
    for i in code:
        cv += ord(i)
        cv *= 17
        cv %= 256
    return cv


cv = 0
for inp in inputs:
    cv += get_value(inp)
print("Part 1: ", cv)


def focus_power(box_number, slot, focal_length):
    return (1 + box_number) * (int(slot) + 1) * focal_length


def parse_input(input):
    for i, char in enumerate(input):
        if char in ["=", "-"]:
            break
    label = input[:i]
    op = input[i]
    param = input[i+1:]

    return label, op, param


boxes = [{} for i in range(256)]
for inp in inputs:
    label, op, param = parse_input(inp)
    print(f"From box {label}, do {op}, with {param}")
    box_number = get_value(label)
    if op == "-":
        if label in boxes[box_number]:
            boxes[box_number].pop(label)
    elif op == "=":
        boxes[box_number][label] = param


print(boxes)
total_power = 0
for i, box in enumerate(boxes):
    for j, label in enumerate(box):
        print(i, j, int(box[label]))
        fp = focus_power(i, j, int(box[label]))
        print(fp)
        total_power += fp

print(total_power)