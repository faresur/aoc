import sys
from math import prod


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as engine:
        schematic: list[str] = [line.strip() for line in engine]

    part_numbers: list[int] = []
    possible_gears: dict = {}

    adjacent_offsets: set[tuple(int)] = {(-1, -1), (-1, 0), (-1, 1),
                                         (0, -1),           (0, 1),
                                         (1, -1),  (1, 0),  (1, 1)}
    current_num: str = ""
    is_part: bool = False
    adjacent_gears: set[str] = set()
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if not char.isnumeric():
                if current_num and is_part:
                    part_numbers.append(int(current_num))
                    for gear in adjacent_gears:
                        try:
                            possible_gears[gear].append(int(current_num))
                        except KeyError:
                            possible_gears[gear] = [int(current_num)]
                current_num = ""
                is_part = False
                adjacent_gears = set()
                continue

            current_num += char
            for o in adjacent_offsets:
                if (i + o[0] < 0 or i + o[0] >= len(schematic)) or\
                   (j + o[1] < 0 or j + o[1] >= len(schematic[0])):
                       continue
                adjacent: str = schematic[i + o[0]][j + o[1]]
                if not adjacent.isnumeric() and adjacent != '.':
                    is_part = True
                if adjacent == '*':
                    adjacent_gears.add((i + o[0], j + o[1]))
    if current_num and is_part:
        part_numbers.append(int(current_num))
        for gear in adjacent_gears:
            try:
                possible_gears[gear].append(int(current_num))
            except KeyError:
                possible_gears[gear] = [int(current_num)]


    print("Part 01:")
    print(f"Answer = {sum(part_numbers)}")

    print()

    gear_ratios: int = 0
    for part_nums in possible_gears.values():
        if len(part_nums) == 2:
            gear_ratios += prod(part_nums)

    print("Part 02:")
    print(f"Answer = {gear_ratios}")


if __name__ == "__main__":
    main()
