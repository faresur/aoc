import sys
from math import prod


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    color_indices: dict = {"red": 0, "green": 1, "blue": 2}

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as game:
        games: list[set] = [parse_game(line.strip(), color_indices)
                            for line in game]

    bag: tuple[int] = (12, 13, 14)
    possible_games: set[int] = {game_is_possible(i + 1, game, bag)
                                for i, game in enumerate(games)}
    sum_of_ids: int = sum(possible_games)

    print("Part 01:")
    print(f"Answer = {sum_of_ids}")

    print()

    cube_powers: list[int] = [calc_cube_powers(game) for game in games]
    sum_of_powers: int = sum(cube_powers)
    print("Part 02:")
    print(f"Answer = {sum_of_powers}")
    

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


def calc_cube_powers(game: set[tuple[int]]) -> int:
    minimum_cubes: list[int] = [0, 0, 0]
    for rnd in game:
        for i in range(len(minimum_cubes)):
            if rnd[i] > minimum_cubes[i] or minimum_cubes[i] == -1:
                minimum_cubes[i] = rnd[i]
    return prod(minimum_cubes)


if __name__ == "__main__":
    main()
