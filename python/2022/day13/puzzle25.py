def convert(nest):
    lists = [[]]
    level = -1
    for i in nest:
        if i == '[':
            level += 1
            lists += [[]]
        elif '0' <= i < ':':
            lists[level] += [int(i)]
        elif i == ']':
            lists[level-1] += [lists[level]]
            del lists[level]
            level -= 1
    return lists[0][0]


def compare(pair):
    out = 0
    left = pair[0]
    right = pair[1]
    if len(right) == 0 and len(left) > 0:
        out = -1
        return out
    elif len(left) == 0 and len(right) > 0:
        out = 1
        return out
    for i in range(len(right)):
        try:
            if type(left[i]) is not type(right[i]):
                if type(left[i]) is list:
                    out = compare([left[i], [right[i]]])
                else:
                    out = compare([[left[i]], right[i]])
                if out != 0:
                    break
                else:
                    continue
            elif type(left[i]) is list:
                out = compare([left[i], right[i]])
                if out != 0:
                    break
                else:
                    continue
            elif left[i] < right[i]:
                out = 1
                break
            elif left[i] > right[i]:
                out = -1
                break
        except IndexError:
            out = 1
            break
    if len(left) > len(right) and out == 0:
        out = -1
    return out
 

def main():
    ind_sum = 0

    with open("input13.txt", 'r') as packets:
        lines = packets.readlines()
        lines = list(map(lambda x: x.strip(), lines))

    packet = [[eval(lines[i]), eval(lines[i+1])] for i in range(0, len(lines), 3)]
    
    for k in range(len(packet)):
        x = compare(packet[k])
        print(k+1, x)
        if x == 1:
            ind_sum += k+1

    print(f"Sum of in-order pair indices: {ind_sum}")


if __name__ == "__main__":
    main()