def main():
    overlap = 0

    with open("input04.txt", 'r') as sections:
        for line in sections:
            pair = line.split(',')
            ran0, ran1 = pair[0].split('-'), pair[1].split('-')
            insection = set(range(int(ran0[0]), int(ran0[1])+1)) & set(range(int(ran1[0]), int(ran1[1])+1)) 
            if len(insection) > 0:
                overlap += 1

    print(f"{overlap} pairs overlap.")


if __name__ == "__main__":
    main()
