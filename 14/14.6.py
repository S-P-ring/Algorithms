class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, n):
        self.items.append(n)
        return "ok"

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        return self.items.pop(0)

    def front(self):
        if len(self.items) == 0:
            return 'error'
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        return "ok"

    def exit(self):
        return 'bye'

    def execute(self, line):
        method, *args = line.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    with open('input1.txt') as file:
        stack = Stack()
        for line in file:
            result = stack.execute(line)
            print(result)
            if result == 'bye':
                break