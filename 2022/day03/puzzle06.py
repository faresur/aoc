def main():
    alph = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    priori = {j: i+1 for i, j in enumerate(alph)}

    total = 0

    with open("input03.txt", 'r') as rucks:
        group = []
        for i, line in enumerate(rucks):
            group.append(line.strip())
            if (i+1) % 3 == 0:
                common = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
                group = []
                total += priori[common]

    print(total)


if __name__ == "__main__":
    main()