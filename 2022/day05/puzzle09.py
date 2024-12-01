"""
    [B]             [B] [S]
    [M]             [P] [L] [B] [J]
    [D]     [R]     [V] [D] [Q] [D]
    [T] [R] [Z]     [H] [H] [G] [C]
    [P] [W] [J] [B] [J] [F] [J] [S]
[N] [S] [Z] [V] [M] [N] [Z] [F] [M]
[W] [Z] [H] [D] [H] [G] [Q] [S] [W]
[B] [L] [Q] [W] [S] [L] [J] [W] [Z]
 1   2   3   4   5   6   7   8   9
"""


def main():
    crate = [[i for i in "BWN"], [i for i in "LZSPTDMB"], [i for i in "QHZWR"],
             [i for i in "WDVJZR"], [i for i in "SHMB"],
             [i for i in "LGNJHVPB"], [i for i in "JQZFHGLS"],
             [i for i in "WSFJGQB"], [i for i in "ZWMSCDJ"]]

    with open("input05.txt", 'r') as crates:
        insts = []
        for line in crates:
            line = line.split()
            nums = []
            for i in line:
                if '0' < i < ':':
                    nums += [int(i)]
            insts += [tuple(nums)]

    for it in insts:
        for i in range(it[0]):
            crate[it[2]-1].append(crate[it[1]-1].pop())

    out = ''
    for i in crate:
        out += i[-1]

    print(f"The final crates on top will be {out}.")


if __name__ == "__main__":
    main()
