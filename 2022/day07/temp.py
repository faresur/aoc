def main():
    sizes = {}
    refs = {}

    with open("input07.txt", 'r') as term:
        cont = False
        pwd = []

        size = 0

        for line in term:
            com = line.strip()
            if cont and com[0] == '$':
                cont = False
                try:
                    sizes[pwd[-1]] += size
                except KeyError:
                    sizes[pwd[-1]] = size
                size = 0

            if cont is False:
                if com == "$ ls":
                    cont = True
                elif com == "$ cd ..":
                    pwd = pwd[:-1]
                elif com[:4] == "$ cd":
                    pwd += [com.split()[2]]
            elif cont:
                part = com.split()
                if part[0] == "dir":
                    try:
                        refs[pwd[-1]] += [part[1]]
                    except KeyError:
                        refs[pwd[-1]] = [part[1]]
                else:
                    size += int(part[0])
        cont = False
        try:
            sizes[pwd[-1]] += size
        except KeyError:
            sizes[pwd[-1]] = size
        size = 0

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
