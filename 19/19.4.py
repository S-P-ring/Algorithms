class Heap:

    def __init__(self):
        self.dict = {}

    def add(self, id, priority):
        self.dict[id] = priority

    def change(self, id, new_priority):
        self.dict[id] = new_priority

    def pop(self):
        maximum = max(self.dict, key=self.dict.get)
        var = self.dict.pop(maximum)
        return maximum, var

    def execute(self, line):
        method, *args = line.lower().split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    h = Heap()
    with open('input.txt') as inp:
        for line in inp:
            var = h.execute(line)
            if var != None:
                print(*var)
