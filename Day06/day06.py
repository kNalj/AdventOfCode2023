with open("day06", "r") as f:
    times, distances = [[int(a) for a in line.strip().split(":")[1].split(" ") if a != ""] for line in f.readlines()]

print(times, distances)

ways = [0] * len(times)
for i, time in enumerate(times):
    for winding_time in range(time):
        if (winding_time * (time - winding_time)) > distances[i]:
            ways[i] += 1

total = 1
for i in ways:
    total *= i

print(total)

time = int("".join([str(time) for time in times]))
distance = int("".join([str(distance) for distance in distances]))

for winding_time in range(time):
    if (winding_time * (time - winding_time)) > distance:
        lower_limit = winding_time
        break

for winding_time in range(time, 0, -1):
    if (winding_time * (time - winding_time)) > distance:
        upper_limit = winding_time
        break


print(upper_limit - lower_limit + 1)

