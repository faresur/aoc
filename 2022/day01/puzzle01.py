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

    print(f"Elf {elves.index(max(elves))+1:02} with {max(elves)} calories.")


if __name__ == "__main__":
    main()
