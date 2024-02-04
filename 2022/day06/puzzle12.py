def main():
    with open("input06.txt", 'r') as buffer:
        inp = buffer.readline()

    for i in range(len(inp)-14):
        if len(list(inp[i:i+14])) == len(set(inp[i:i+14])):
            chars = i+14
            break

    print(f"First marker after character {chars}.")


if __name__ == "__main__":
    main()
