def main():
    high = 0

    with open("example.txt", 'r') as trees:
        hor = [line.strip() for line in trees]

        coords = []

        for i in range(1, len(hor)-1):
            row = [int(k) for k in hor[i]]
            for j in range(1, len(hor[i])-1):
                comp = int(hor[i][j])
                col = [int(l[j]) for l in hor]

                if (comp == max(row[j:]) and row[j:].count(comp) == 1) or (comp == max(row[:j+1]) and row[:j+1].count(comp) == 1):
                    coords += [(comp, j, i)]
                elif (comp == max(col[i:]) and col[i:].count(comp) == 1) or (comp == max(col[:i+1]) and col[:i+1].count(comp) == 1):
                    coords += [(comp, j, i)]
    
    for i in coords:
        tot = 1 
        h = i[0]
        for j in range(4):
            curr = 0
            r, c = i[2], i[1]
            while 0 < r < len(hor[0])-1:
                r -= 1
                if int(hor[r][c]) < h:
                    curr += 1
                else:
                    break
            tot *= curr
        
        if tot > high:
            high = tot
        

    print(high)


if __name__ == "__main__":
    main()