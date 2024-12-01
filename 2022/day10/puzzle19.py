class CPU:
    def __init__(self, mem):
        self.x = 1
        self.signal = 0
        self.clock = 1
        self.prog = 0
        self.inc = 0
        self.mem = mem
        self.storage = 0

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

    def boot(self, *points):
        ind = 0
        while self.clock <= points[-1] and self.inc < len(self.mem):
            # fetch from memory
            com = self.fetch()
            self.signal = self.clock * self.x
            # check current signal strength
            if self.clock == points[ind]:
                self.storage += self.signal
                print(f"Cycle {self.clock}: register X = {self.x}, signal strength = {self.signal}.")
                ind += 1
            # execute
            self.exec(com)
            self.clock += 1


def main():
    with open("input10.txt", 'r') as insructions:
        inst = list(map(lambda x: x.strip(), insructions.readlines()))
    
    comp = CPU(inst)
    comp.boot(20, 60, 100, 140, 180, 220)

    print(f"Sum of checked signal strengths: {comp.storage}")

if __name__ == "__main__":
    main()