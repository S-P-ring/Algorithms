class Stack:

    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        del self.items[-1]

    def get_min(self):
        return min(self.items)

    def execute(self, method, *args):
        return getattr(self, method)(*args)


if __name__ == '__main__':
    stack = Stack()
    functions = {1: 'push', 2: 'pop', 3: 'get_min'}
    n = int(input())
    for i in range(n):
        func = [int(x) for x in input().split()]
        try:
            result = stack.execute(functions[func[0]], func[1])
        except IndexError:
            result = stack.execute(functions[func[0]])

        if result != None:
            print(result)
