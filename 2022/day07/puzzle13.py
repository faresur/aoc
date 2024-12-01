def main():
    sizes = {}
    refs = {}

    with open("input07.txt", 'r') as term:
        pwd = []

        for line in term:
            com = line.split()
            if com[0] == '$':
                if com[-1] == "..":
                    pwd = pwd[:-1]
                elif com[1] == "cd":
                    pwd += [com[2]]
            else:
                if com[0] == "dir":
                    try:
                        refs["".join(pwd)] += ["".join(pwd)+com[1]]
                    except KeyError:
                        refs["".join(pwd)] = ["".join(pwd)+com[1]]
                else:
                    try:
                        sizes["".join(pwd)] += int(com[0])
                    except KeyError:
                        sizes["".join(pwd)] = int(com[0])

    for key in reversed(refs.keys()):
        try:
            for i in refs[key]:
                sizes[key] += sizes[i]
        except KeyError:
            pass

    print(sizes)
    print(refs)

    total = 0

    for i in sizes.values():
        if i <= 100000:
            total += i

    print(total)


if __name__ == "__main__":
    main()
