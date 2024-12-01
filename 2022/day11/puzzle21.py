class Monkey:
    def __init__(self, items, operation, div, true, false):
        self.inspections = 0
        self.items = items
        self.operation = operation
        self.div = div
        self.true = true
        self.false = false

    def inspect(self):
        for item in self.items:
            if item % self.div:
                return self.true
            else:
                return self.false

    def yeet(self):
        pass

    def yoink(self):
        pass


def main():
    mon = []
    inspections = []
    
    with open("input11.txt", 'r') as monkeys:
        formula = {"items": [], "operation": [], "cond": int, 'true': int, 'false': int}
        nex = 0
        for line in monkeys:
            if nex % 7 == 1:
                try:
                    formula["items"] = list(map(int, line[18:].split(", ")))
                except ValueError:
                    formula["items"] = [int(line[18:])]
            elif nex % 7 == 2:
                formula["operation"] = line.strip()[20:].split()
            elif nex % 7 == 3:
                formula["cond"] = int(line.split()[-1])
            elif nex % 7 == 4:
                formula['true'] = int(line.split()[-1])
            elif nex % 7 == 5:
                formula['false'] = int(line.split()[-1])
                mon.append(formula.copy())
                inspections.append(0)
            nex += 1

    for i in range(20):
        for j, monkey in enumerate(mon):
            temp = monkey["items"][:]
            for item in temp:
                pretend = item
                if monkey["operation"][-1] == 'old':
                    add = item
                else:
                    add = int(monkey["operation"][-1])
                if monkey["operation"][0] == '*':
                    item *= add
                else:
                    item += add
                item //= 3
                if item % monkey["cond"] == 0:
                    mon[monkey["true"]]["items"] += [item]
                else:
                    mon[monkey["false"]]["items"] += [item]
                del monkey["items"][monkey["items"].index(pretend)]
                inspections[j] += 1

    for i in range(len(inspections)):
        print(f"Monkey {i} inspected items {inspections[i]} times.")                

    temp = sorted(inspections)
    print(f"The level of monkey business: {temp[-1] * temp[-2]}")

if __name__ == "__main__":
    main()