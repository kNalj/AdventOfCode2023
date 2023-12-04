with open("day04", "r") as f:
    lines = [[side.split(" ") for side in line.strip().split(": ")[1].split(" | ")] for line in f.readlines()]

total = 0
cards = {
    i: 1 for i in range(len(lines))
}
print(cards)

for i, [ticket, winners] in enumerate(lines):
    ticket = [int(num) for num in ticket if num != '']
    winners = [int(num) for num in winners if num != '']
    lines[i] = [ticket, winners]

    pow = -1
    for num in ticket:
        if num in winners:
            pow += 1

    total += (2**pow) if (pow > -1) else 0
    for x in range(i+1, min(i + max(pow, 0) + 2, len(lines))):
        cards[x] += 1 * cards[i] if pow > -1 else 0


print(total)
print(sum(cards.values()))
