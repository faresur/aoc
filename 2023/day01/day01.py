import sys
import re


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as input_file:
        lines: list[str] = input_file.readlines()

    mappings: dict = {"one": '1', "two": '2', "three": '3',
                      "four": '4', "five": '5', "six": '6',
                      "seven": '7', "eight": '8', "nine": '9'}


    calibration_values: list[int] = (get_value(line) for line in lines)
    total_value: int = sum(calibration_values)
    
    print("Part 1:")
    print(f"Answer = {total_value}")

    print()

    spelled_values: list[int] = (get_spelled_value(line, mappings)
                                 for line in lines)
    total_spelled_value: int = sum(spelled_values)

    print("Part 2:")
    print(f"Answer = {total_spelled_value}")
    

def get_value(line: str) -> int:
    regex: str = r"(?=(\d))"
    digits: str = ''.join(re.findall(regex, line))
    return int(digits[0] + digits[-1])

def get_spelled_value(line: str, mappings: dict) -> str:
    regex: str = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    digits: str = ''.join(mappings[digit] if digit in mappings else digit
                          for digit in re.findall(regex, line))
    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    main()
