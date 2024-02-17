class CRT:
    def __init__(self, on='#', off='.'):
        self.on = on
        self.off = off
        self.screen = [[self.off for i in range(40)] for i in range(6)]
        self.pixel = [0, 0]
        self.max_x = 40
        self.max_y = 6

    def __str__(self):
        return '\n'.join(map(lambda x: "".join(x), self.screen))

    def draw(self, sprite):
        if sprite - 1 <= self.pixel[0] <= sprite + 1:
            self.screen[self.pixel[1]][self.pixel[0]] = self.on
        else:
            self.screen[self.pixel[1]][self.pixel[0]] = self.off
        if self.pixel[0] < self.max_x-1:
            self.pixel[0] += 1
        else:
            self.pixel[0] = 0
            self.pixel[1] += 1


class CPU:
    def __init__(self, mem, scr):
        self.x = 1
        self.signal = 0
        self.clock = 1
        self.prog = 0
        self.inc = 0
        self.mem = mem
        self.screen = scr

    def fetch(self):
        # fetch instruction
        com = self.mem[self.inc]
        # decode instruction
        if com[:4] == "addx":
            self.prog += 1
        return com

    def exec(self, command):
        # execute instruction
        if command == "noop":
            self.inc += 1
        else:
            if self.prog == 2:
                command = command.split()
                command[-1] = int(command[-1])
                self.prog = 0
                self.x += command[-1]
                self.inc += 1

    def boot(self):
        while self.inc < len(self.mem):
            # fetch from memory
            com = self.fetch()
            # draw
            self.screen.draw(self.x)
            # execute
            self.exec(com)
            self.clock += 1


def main():
    with open("input10.txt", 'r') as insructions:
        inst = list(map(lambda x: x.strip(), insructions.readlines()))

    comp = CPU(inst, CRT(on=chr(9608), off=' '))
    comp.boot()

    print(comp.screen)


if __name__ == "__main__":
    main()
