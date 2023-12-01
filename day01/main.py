import sys


def get_value(line: str) -> int:
    digits: list[str] = [char for char in line if char.isnumeric()]
    try:
        return int(digits[0] + digits[-1])
    except IndexError:
        return 0


def replace_spelled(line: str) -> str:
    pass


def main() -> None:
    file_path: str = sys.argv[1]

    with open(file_path, 'r') as input_file:
        sum_of_values: int = sum(map(get_value, input_file.readlines()))

    print(sum_of_values)
    


if __name__ == "__main__":
    main()
