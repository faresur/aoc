import sys
from math import prod


def main() -> None:
    color_indices: dict = {"red": 0, "green": 1, "blue": 2}

    part01_path: str = sys.argv[1]
    with open(part01_path, 'r') as game01:
        games01: list[set] = [parse_game(line.strip(), color_indices)
                            for line in game01]

    bag: tuple[int] = (12, 13, 14)
    possible_games: list[int] = {game_is_possible(i + 1, game, bag)
                                for i, game in enumerate(games01)}

    print("Part 01:")
    print(f"Answer = {sum(possible_games)}")

    print()

    part02_path: str = sys.argv[2]
    with open(part02_path, 'r') as game02:
        games02: list[set] = [parse_game(line.strip(), color_indices)
                            for line in game02]

    answer: int = sum((power_of_game_cubes(game) for game in games02))
    print("Part 02:")
    print(f"Answer = {answer}")
    

def parse_game(game_string: str, color_ind: dict) -> set[tuple[int]]:
    rounds: list[str] = game_string.split(": ")[1].split("; ")

    cube_combos: set[tuple[int]] = set()
    for current_round in rounds:
        round_colors: list = [0, 0, 0]
        for cubes in current_round.split(", "):
            amount, color = cubes.split(' ')
            round_colors[color_ind[color]] = int(amount)
        cube_combos.add(tuple(round_colors))

    return cube_combos


def game_is_possible(game_id: int, game: tuple, bag_combo: tuple) -> int:
    for game_combo in game:
        for i, j in zip(game_combo, bag_combo):
            if i > j:
                return 0
    return game_id


def power_of_game_cubes(game: set[tuple[int]]) -> int:
    minimum_cubes: list[int] = [0, 0, 0]
    for rnd in game:
        for i in range(len(minimum_cubes)):
            if rnd[i] > minimum_cubes[i] or minimum_cubes[i] == -1:
                minimum_cubes[i] = rnd[i]
    return prod(minimum_cubes)


if __name__ == "__main__":
    main()
