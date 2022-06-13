class Stack:

    def __init__(self):
        n = 150000
        self.items = []
        for i in range(n):
            self.items.append([0] * 1)

    def pushfront(self, a, b):
        if self.items[a][0] == 0:
            self.items[a][0] = b
        else:
            self.items[a].insert(0, b)

    def pushback(self, a, b):
        if self.items[a][0] == 0:
            self.items[a][0] = b
        else:
            self.items[a].append(b)

    def popfront(self, a):
        if len(self.items) == 0:
            return ''
        return self.items[a].pop(0)

    def popback(self, a):
        if len(self.items) == 0:
            return ''
        return self.items[a].pop()

    def execute(self, method, args):
        return getattr(self, method)(*args)


if __name__ == '__main__':
    n = int(input())
    stack = Stack()
    for _ in range(n):
        all_info = input().split()
        name = all_info[0]
        args = [int(x) for x in all_info[1:]]
        result = stack.execute(name, args)
        if result != None:
            print(result)

