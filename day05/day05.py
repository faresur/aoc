import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as input_file:
        almanac: list[str] = [line.strip() for line in input_file]

    seeds: list[int] = [int(i) for i in almanac[0].split()[1:]]
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

    locations: list[int] = []

    for seed in seeds:
        mapped_val: int = seed
        for mapping in maps:
            for dest, src, rng in mapping:
                if src <= mapped_val < src + rng:
                    mapped_val = dest + mapped_val - src
                    break
        locations.append(mapped_val)
    
    nearest_location: int = min(locations)

    print("Part 1:")
    print(f"Answer = {nearest_location}")


if __name__ == "__main__":
    main()
