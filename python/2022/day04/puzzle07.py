def main():
    contained = 0

    with open("input04.txt", 'r') as sections:
        for line in sections:
            pair = line.split(',')
            ran0, ran1 = pair[0].split('-'), pair[1].split('-')
            set0, set1 = set(range(int(ran0[0]), int(ran0[1])+1)), set(range(int(ran1[0]), int(ran1[1])+1)) 
            insection = set0 & set1
            if len(insection) == len(set0) or len(insection) == len(set1):
                contained += 1

    print(f"In {contained} pairs one range is contained.")


if __name__ == "__main__":
    main()
