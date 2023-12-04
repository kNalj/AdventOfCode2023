with open("scratch_6.txt", 'r') as f:
    strings = [''.join([char for char in line if char.isdigit()]) for line in f.readlines()]

nums = [int(s[0] + s[-1]) for s in strings]
print(sum(nums))

ad = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("scratch_6.txt", 'r') as f:
    lines = []
    for line in f.readlines():
        line = line.strip()
        inds = []
        for r in ad:
            inds += [(i, r) for i in range(len(line)) if line.startswith(r, i)]
        inds = sorted(inds, reverse=True)
        for i, v in inds:
            line = line[0:i] + ad[v] + line[i:]
        fixed = ''.join([char for char in line if char.isdigit()])
        lines.append(fixed)


nums = [int(s[0] + s[-1]) for s in lines]
print(sum(nums))