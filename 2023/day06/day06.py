import sys
from math import prod


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as inp:
        times: list[str] = inp.readline().split()[1:]
        distances: list[str] = inp.readline().split()[1:]

    races: list[tuple[int]] = zip(map(int, times), map(int, distances))
    margins: list[int] = [calc_margin(t, d) for t, d in races]

    final_margin: int = prod(margins)
    print("Part 01:")
    print(f"Answer = {final_margin}")

    print()

    time: int = int(''.join(times))
    distance: int = int(''.join(distances))
    margin: int = calc_margin(time, distance)
    print("Part 02:")
    print(f"Answer = {margin}")


def calc_margin(time: int, distance: int) -> int:
    race_margin: list[int] = [speed for speed in range(time)
                              if speed * (time - speed) > distance]
    return len(race_margin)



if __name__ == "__main__":
    main()
