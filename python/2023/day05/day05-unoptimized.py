import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as input_file:
        almanac: list[str] = [line.strip() for line in input_file]


    maps: list[set[tuple[int]]] = generate_maps(almanac)

    seeds: list[int] = [int(seed) for seed in almanac[0].split()[1:]]
    locations: list[int] = get_locations(seeds, maps)
    nearest_location: int = min(locations)

    print("Part 1:")
    print(f"Answer = {nearest_location}")

    seed_ranges: list[int] = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    locations: list[int] = get_ranged_locations(seed_ranges, maps)


def generate_maps(almanac: list[str]) -> list[set[tuple[int]]]:
    maps: list[set[tuple[int]]] = []
    current_map: set[tuple[int]] = set()
    for line in almanac[2:]:
        if not line:
            maps.append(current_map)
            current_map = set()
            continue
        if line[-4:] == "map:":
            continue
        map_rule: tuple[int] = tuple(map(int, line.split()))
        current_map.add(map_rule)
    maps.append(current_map)
    return maps


def get_locations(seeds: list[int],
                  maps: list[set[tuple[int]]]) -> list[int]:
    locations: list[int] = []
    for seed in seeds:
        mapped_val: int = seed
        for mapping in maps:
            for dest, src, rng in mapping:
                if src <= mapped_val < src + rng:
                    mapped_val = dest + mapped_val - src
                    break
        locations.append(mapped_val)
    return locations


def get_ranged_locations(seed_ranges: list[tuple[int]],
                         maps: list[set[tuple[int]]]) -> list[int]:
    locations_ranges: list[tuple[int]] = []
    for seedrng in seed_ranges:
        unmapped_vals: list[tuple[int]] = [seedrng]
        mapped_vals: list[tuple[int]] = []
        for mapping in maps:
            for dest, src, rng in mapping:
                pass


def map_range(input_range: tuple[int],
              from_range: tuple[int],
              to_range: tuple[int]):
    pass


if __name__ == "__main__":
    main()
