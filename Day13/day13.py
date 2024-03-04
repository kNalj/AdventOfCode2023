with open("day13", "r") as f:
    patterns = [pattern.split("\n") for pattern in f.read().split("\n\n")]


def almost_same(a, b, diffs=1):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return diffs == d


def is_mirror(pattern, lower, upper, size, diffs=1):
    d = 0
    l = pattern[lower-(size - 1):lower+1]
    u = pattern[upper: upper+mirror_length][::-1]
    for i in range(len(l)):
        if l[i] != u[i]:
            d += 1

    return d == diffs


s = 0
lns = 0
for p, pattern in enumerate(patterns):
    columns = []
    for j in range(len(pattern[0])):
        columns.append("".join([row[j] for row in pattern]))

    for i in range(len(columns)):
        found = False
        for j in range(i+1, len(columns)):
            if found:
                break
            if almost_same(columns[i], columns[j]):
                lower = (i + j) // 2
                upper = (i + j) // 2 + 1
                mirror_length = min(lower + 1, len(columns) - (lower + 1))
                if is_mirror(columns, lower, upper, mirror_length):
                    if (j - i) % 2:
                        lns += 1
                        s += lower + 1
                        found = True
        if found:
            break

    for i in range(len(pattern)):
        found = False
        for j in range(i+1, len(pattern)):
            if found:
                break
            if almost_same(pattern[i], pattern[j]):
                lower = (i + j) // 2
                upper = (i + j) // 2 + 1
                mirror_length = min(lower + 1, len(pattern) - (lower + 1))
                if is_mirror(pattern, lower, upper, mirror_length):
                    if (j - i) % 2:
                        lns += 1
                        s += 100 * (lower + 1)
                        found = True
        if found:
            break

print(s)
