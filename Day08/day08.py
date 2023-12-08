with open("day08", "r") as f:
    path = [a for a in f.readline().strip()]

    nodes = {line.split(" = ")[0]: line.strip().split(" = ")[1].strip("()").split(", ") for line in f.readlines() if line.strip() != ""}

current = "AAA"
steps = 0
while current != "ZZZ":
    for i in path:
        steps += 1
        if i == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]

print("Part 1 solution: ", current)

current_list = [node for node in nodes if node[-1] == "A"]
cl = []
for current in current_list:
    steps = 0
    while current[-1] != "Z":
        for i in path:
            steps += 1
            if i == "L":
                current = nodes[current][0]
            else:
                current = nodes[current][1]

    cl.append(steps)


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

lcm = 1
for i in cl:
    lcm = lcm * i // gcd(lcm, i)

print("Part 2 solution: ", lcm)
