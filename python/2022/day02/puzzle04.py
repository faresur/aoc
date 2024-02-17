def main():
    lose = {'A': 'C', 'B': 'A', 'C': 'B'}
    draw = {'A': 'A', 'B': 'B', 'C': 'C'}
    win = {'A': 'B', 'B': 'C', 'C': 'A'}
    eqs = {'X': lose, 'Y': draw, 'Z': win}
    vals = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}

    with open('input02.txt', 'r') as strat:
        rounds = [line.split() for line in strat]

    total = 0

    for rnd in rounds:
        x, y = rnd[0], rnd[1]
        total += vals[eqs[y][x]] + vals[y]

    print(f"Total score: {total}")


if __name__ == "__main__":
    main()
