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


def prev_to_next_seed(source, destination_data):
    for destination in destination_data:
        if (source >= destination[1]) and (source < (destination[1] + destination[2])):
            return destination[0] + source - destination[1], destination[2]
    return source, 0


locations = []

for seed in seeds:
    locations.append(find_lowest(seed))

print(min(locations))
