import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as cards:
        points_won: int = sum((get_points(card.strip()) for card in cards))

    print("Part 1:")
    print(f"Answer = {points_won}")

    print()

    with open(input_path, 'r') as pile:
        cards: list[str] = [line.strip() for line in pile]

    amount_of_each_card: list[int] = process_cards(cards)
    amount_of_cards: int = sum(amount_of_each_card)

    print("Part 2:")
    print(f"Answer = {amount_of_cards}")


def get_points(card: str) -> int:
    first_nums, second_nums = card.split(": ")[1].split(" | ")
    
    winning_nums: set[int] = {int(i) for i in first_nums.split()}
    owned_nums: set[int] = {int(i) for i in second_nums.split()}
    
    common_nums: set[int] = winning_nums & owned_nums
    return int(2 ** (len(common_nums) - 1))


def process_cards(cards: list[str]) -> list[int]:
    amount_of_each: list[int] = [1 for _ in range(len(cards))]
    for i, card in enumerate(cards):
        first_nums, second_nums = card.split(": ")[1].split(" | ")
        winning_nums: set[int] = {int(i) for i in first_nums.split()}
        owned_nums: set[int] = {int(i) for i in second_nums.split()}
        common_nums: set[int] = winning_nums & owned_nums
        for j in range(i + 1, i + len(common_nums) + 1):
            amount_of_each[j] += amount_of_each[i]
    return amount_of_each


if __name__ == "__main__":
    main()
