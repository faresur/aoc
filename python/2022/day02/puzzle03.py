def main():
    eqs = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    vals = {'A': 1, 'B': 2, 'C': 3}
    poss = {"BA": 6, "CB": 6, "AC": 6}

    with open('input02.txt', 'r') as strat:
        rounds = [line.split() for line in strat]

    total = 0

    for rnd in rounds:
        x, y = rnd[0], eqs[rnd[1]]
        if x == y:
            total += 3 + vals[y]
            continue
        try:
            poss[f"{x}{y}"]
            total += vals[y]
        except KeyError:
            poss[f"{y}{x}"]
            total += 6 + vals[y]

    print(f"Total score: {total}")


if __name__ == "__main__":
    main()
