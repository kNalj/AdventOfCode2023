import re

with open("example", "r") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]

print(lines)

for i in range(len(lines)):
    lines[i][0] = lines[i][0].replace("?", "#")
    lines[i].append([int(i)*"#" for i in lines[i][1].replace(",", ".") if i != "."])

print(lines)