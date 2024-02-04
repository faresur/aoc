def main():
    elves = []

    with open("input01.txt", 'r') as cals:
        elf = 0
        for line in cals:
            try:
                elf += int(line.strip())
            except ValueError:
                elves.append(elf)
                elf = 0
        elves.append(elf)

    total = 0
    for i in range(1, 4):
        ind = elves.index(max(elves))
        maxim = elves.pop(ind)
        print(f"{i}. place: elf {ind+1:02} with {maxim} calories.")
        total += maxim

    print(f"Top 3 elves have {total} calories.")


if __name__ == "__main__":
    main()
