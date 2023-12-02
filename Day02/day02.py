with open("day02", "r") as f:
    games = [[{pair.split(" ")[1]: int(pair.split(" ")[0]) for pair in rnd.split(", ")} for rnd in line.strip().split(": ")[1].split("; ")] for line in f.readlines()]

limits = {
    "blue": 14,
    "red": 12,
    "green": 13
}

total = 0
for i, game in enumerate(games):
    possible = True
    for round in game:
        for key in limits:
            if key in round:
                if round[key] > limits[key]:
                    possible = False
    if possible:
        total += i+1


print("Part 1 solution: ", total)

power = 0
for game in games:
    min_vals = {
        "blue": 0,
        "red": 0,
        "green": 0
    }
    for round in game:
        for key in round:
            min_vals[key] = max(min_vals[key], round[key])

    curr_power = 1
    for k in min_vals:
        curr_power *= min_vals[k]

    power += curr_power

print("Part 2 solution: ", power)
