import sys
from functools import cmp_to_key


def main() -> None:
    if len(sys.argv) != 2:
        print("Bad arguments!")
        exit(1)

    input_path: str = sys.argv[1]
    with open(input_path, 'r') as inp:
        hand_bids: list[str, int] = {hand[0]: int(hand[1])
                                     for line in inp
                                     if (hand := line.split())}

    hands: list[int] = list(hand_bids.keys())
    hands.sort(key=cmp_to_key(cmp_hands))

    total_winnings: int = 0
    for i, hand in enumerate(hands):
        total_winnings += (i + 1) * hand_bids[hand]

    print("Part 01:")
    print(f"Answer = {total_winnings}")

    joker_hands: list[int] = list(hand_bids.keys())
    joker_hands.sort(key=cmp_to_key(cmp_hands_joker))

    total_winnings_joker: int = 0
    for i, hand in enumerate(joker_hands):
        total_winnings_joker += (i + 1) * hand_bids[hand]

    print("Part 02:")
    print(f"Answer = {total_winnings_joker}")




def evaluate_hand(hand: str) -> int:
    types: dict[tuple, int] = {(0, 0, 0, 0, 1): 7, (1, 0, 0, 1, 0): 6,
                               (0, 1, 1, 0, 0): 5, (2, 0, 1, 0, 0): 4,
                               (1, 2, 0, 0, 0): 3, (3, 1, 0, 0, 0): 2,
                               (5, 0, 0, 0, 0): 1}
    char_freq: dict[str, int] = {}
    for char in hand:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    freq_of_freq: list[int] = [0 for i in range(5)]
    for freq in char_freq.values():
        freq_of_freq[freq - 1] += 1

    return types[tuple(freq_of_freq)]


def cmp_hands(hand1: str, hand2: str, el=True) -> int:
    card_values: dict[str, int] = {'2': 2, '3': 3, '4': 4, '5': 5,
                                   '6': 6, '7': 7, '8': 8, '9': 9,
                                   'T': 10, 'J': 11, 'Q': 12, 'K': 13,
                                   'A': 14}
    hand1_val: int = evaluate_hand(hand1)
    hand2_val: int = evaluate_hand(hand2)
    if hand1_val < hand2_val:
        return -1
    if hand1_val > hand2_val:
        return 1
    for char1, char2 in zip(hand1, hand2):
        if card_values[char1] < card_values[char2]:
            return -1
        if card_values[char1] > card_values[char2]:
            return 1
    return 0



def eval_hand_joker(hand: str) -> int:
    types: dict[tuple, int] = {(0, 0, 0, 0, 1): 7, (1, 0, 0, 1, 0): 6,
                               (0, 1, 1, 0, 0): 5, (2, 0, 1, 0, 0): 4,
                               (1, 2, 0, 0, 0): 3, (3, 1, 0, 0, 0): 2,
                               (5, 0, 0, 0, 0): 1}
    js: int = 0
    char_freq: dict[str, int] = {}
    for char in hand:
        if char == 'J':
            js += 1
        elif char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    freq_of_freq: list[int] = [0 for i in range(5)]
    for freq in char_freq.values():
        freq_of_freq[freq - 1] += 1

    for i in range(len(freq_of_freq) - 2, -1, -1):
        if freq_of_freq[i]:
            freq_of_freq[i+js] += 1
            freq_of_freq[i] -= 1
            break
    else:
        freq_of_freq[-1] += 1

    return types[tuple(freq_of_freq)]


def cmp_hands_joker(hand1: str, hand2: str) -> int:
    card_values: dict[str, int] = {'J': 1, '2': 2, '3': 3, '4': 4,
                                   '5': 5, '6': 6, '7': 7, '8': 8,
                                   '9': 9, 'T': 10, 'Q': 11, 'K': 12,
                                   'A': 13}
    hand1_val: int = eval_hand_joker(hand1)
    hand2_val: int = eval_hand_joker(hand2)
    if hand1_val < hand2_val:
        return -1
    if hand1_val > hand2_val:
        return 1
    for char1, char2 in zip(hand1, hand2):
        if card_values[char1] < card_values[char2]:
            return -1
        if card_values[char1] > card_values[char2]:
            return 1
    return 0


if __name__ == "__main__":
    main()
