def main():
    alph = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    priori = {j: i+1 for i, j in enumerate(alph)}

    total = 0

    with open("input03.txt", 'r') as rucks:
        for line in rucks:
            cont = line.strip()
            mid = len(cont)//2
            comp0, comp1 = cont[:mid], cont[mid:]
            mis = list(set(comp0) & set(comp1))[0]
            total += priori[mis]

    print(total)


if __name__ == "__main__":
    main()