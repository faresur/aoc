import sys
import re


def main() -> None:
    if len(sys.argv) != 3:
        print("Bad arguments!")
        exit(1)

    part01_path: str = sys.argv[1]
    part02_path: str = sys.argv[2]

    mappings: dict = {"one": '1', "two": '2', "three": '3',
                      "four": '4', "five": '5', "six": '6',
                      "seven": '7', "eight": '8', "nine": '9'}

    with open(part01_path, 'r') as input_file:
        lines01: list[str] = input_file.readlines()

    answer01: int = sum((get_value(line) for line in lines01))

    print(f"Answer to part 1:\n{answer01}")

    with open(part02_path, 'r') as input_file:
        lines02: list[str] = input_file.readlines()

    answer02: int = sum((get_spelled_value(line,
                                           mappings
                                           ) for line in lines01))

    print(f"Answer to part 2:\n{answer02}")
    

def get_value(line: str) -> int:
    digits: list[str] = [char for char in line if char.isnumeric()]
    try:
        return int(digits[0] + digits[-1])
    except IndexError:
        return 0

def get_spelled_value(line: str, mappings: dict) -> str:
    regex: str = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    digits: str = ''.join(mappings[dig] if dig in mappings else dig
                          for dig in re.findall(regex, line))
    if not digits:
        return 0
    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    main()
