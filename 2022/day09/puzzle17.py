class knot:
    def __init__(self):
        self.coords = [0, 0]
        self.been = {(0, 0)}

    def __str__(self):
        return str(tuple(self.coords))
    
    __repr__ = __str__
    
    def move(self, dr):
        for i in dr:
            if i == 'U':
                self.coords[1] += 1
            elif i == 'D':
                self.coords[1] -= 1
            elif i == 'R':
                self.coords[0] += 1
            elif i == 'L':
                self.coords[0] -= 1
    
    def follow(self, pos):
        d = ((self.coords[0]-pos[0])**2+(self.coords[1]-pos[1])**2)**(1/2)
        if d > 2**(1/2):
            if self.coords[0] < pos[0]:
                self.move('R')
            elif self.coords[0] > pos[0]:
                self.move('L')
            if self.coords[1] < pos[1]:
                self.move('U')
            elif self.coords[1] > pos[1]:
                self.move('D')
        self.been = self.been | {tuple(self.coords)}


def main():
    h, t = knot(), knot()
    with open("input09.txt", 'r') as insts:
        for line in insts:
            ins = line.split()
            for i in range(int(ins[1])):
                h.move(ins[0])
                t.follow(h.coords)
    print(t.been)
    print(len(t.been))


if __name__ == "__main__":
    main()