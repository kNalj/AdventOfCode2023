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


def prev_to_next_range(sources, destinations):
    next_ranges = []
    for i in range(0, len(sources), 2):
        ranges = [[sources[i], sources[i] + sources[i+1]]]
        while ranges:
            range_start, range_end = ranges.pop()
            for destination in destinations:
                end_map = destination[1] + destination[2]
                offset = destination[0] - destination[1]
                if end_map <= range_start or range_end <= destination[1]:
                    continue
                if range_start < destination[1]:
                    ranges.append([range_start, destination[1]])
                    range_start = destination[1]
                if end_map < range_end:
                    ranges.append([end_map, range_end])
                    range_end = end_map
                next_ranges.append(range_start + offset)
                next_ranges.append(range_end + offset - (range_start + offset))
                break
            else:
                next_ranges.append(range_start)
                next_ranges.append(range_end - range_start)
    return next_ranges

# print(seeds)
soils = prev_to_next_range(seeds, data["seed-to-soil"])
# print(soils)
fertilizers = prev_to_next_range(soils, data["soil-to-fertilizer"])
# print(fertilizers)
waters = prev_to_next_range(fertilizers, data["fertilizer-to-water"])
# print(waters)
lights = prev_to_next_range(waters, data["water-to-light"])
# print(lights)
temperatures = prev_to_next_range(lights, data["light-to-temperature"])
# print(temperatures)
humidities = prev_to_next_range(temperatures, data["temperature-to-humidity"])
# print(humidities)
locations = prev_to_next_range(humidities, data["humidity-to-location"])
# print(locations)

print(min([locations[i] for i in range(0, len(locations), 2)]))

# 3832413546 is too high

