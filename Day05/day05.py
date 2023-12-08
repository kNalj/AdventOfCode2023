with open("day05", "r") as f:
    seeds = [int(seed) for seed in f.readline().strip().split(": ")[1].split(" ")]
    data = f.read().split("\n\n")
data = {d.strip().split(" map:")[0]: [[int(n) for n in l.split(" ")] for l in d.strip().split(" map:")[1].strip().split("\n")] for d in data}


def prev_to_next(source, destination_data):
    for destination in destination_data:
        if (source >= destination[1]) and (source < (destination[1] + destination[2])):
            return destination[0] + source - destination[1]
    return source


def find_lowest(seed):
    soil = prev_to_next(seed, data["seed-to-soil"])
    fertilizer = prev_to_next(soil, data["soil-to-fertilizer"])
    water = prev_to_next(fertilizer, data["fertilizer-to-water"])
    light = prev_to_next(water, data["water-to-light"])
    temperature = prev_to_next(light, data["light-to-temperature"])
    humidity = prev_to_next(temperature, data["temperature-to-humidity"])
    location = prev_to_next(humidity, data["humidity-to-location"])
    # print(f"{seed} -> {fertilizer} -> {water} -> {light} -> {temperature} -> {humidity} -> {location}")
    return location


locations = []

for seed in seeds:
    locations.append(find_lowest(seed))

print(min(locations))
print()


def extract_points_of_interest(data):
    points = []
    for i in data:
        points.append(i[1])
        points.append(i[1] + i[2])
    return sorted(list(set(points)))


def build_reverse_map():
    h = extract_points_of_interest(data["humidity-to-location"])
    t = extract_points_of_interest(data["temperature-to-humidity"])
    l = extract_points_of_interest(data["light-to-temperature"])
    w = extract_points_of_interest(data["water-to-light"])
    f = extract_points_of_interest(data["fertilizer-to-water"])
    s = extract_points_of_interest(data["soil-to-fertilizer"])
    seed = extract_points_of_interest(data["seed-to-soil"])

    return seed, s, f, w, l, t, h


rmap = build_reverse_map()
print(rmap)
