def main():

    with open("input08.txt", 'r') as trees:
        hor = [line.strip() for line in trees]

        vis = len(hor[0])*2 + len(hor)*2 - 4

        for i in range(1, len(hor)-1):
            row = [int(k) for k in hor[i]]
            for j in range(1, len(hor[i])-1):
                comp = int(hor[i][j])
                col = [int(l[j]) for l in hor]

                if (comp == max(row[j:]) and row[j:].count(comp) == 1) or (comp == max(row[:j+1]) and row[:j+1].count(comp) == 1):
                    vis += 1
                elif (comp == max(col[i:]) and col[i:].count(comp) == 1) or (comp == max(col[:i+1]) and col[:i+1].count(comp) == 1):
                    vis += 1
        
        print(f"Number of visible trees: {vis}.")


if __name__ == "__main__":
    main()