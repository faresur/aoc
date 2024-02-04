from dataclasses import dataclass
import sys


@dataclass
class Node:
    value: str
    left: 'Node' = None
    right: 'Node' = None


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]

    nodes: dict[str, Node]


if __name__ == "__main__":
    main()
