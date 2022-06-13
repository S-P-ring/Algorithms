class Stack:

    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def show(self):
        return self.items

    def pop(self):
        self.items.pop()

    def empty(self):
        if len(self.items) == 0:
            return True
        return False

    def clear(self):
        self.items.clear()


if __name__ == '__main__':
    stack = Stack()
    duz = [x for x in input()]
    n = int(input())

    for i in range(0, n):
        a = int(input())

        if duz[a] == '(':
            duz[a] = ')'
        else:
            duz[a] = '('

        b = 0
        for bracket in duz:
            if bracket == '(':
                stack.push(bracket)
            else:
                if stack.empty():
                    print('-')
                    stack.clear()
                    b += 1
                    break
                else:
                    stack.pop()
        if b == 0:
            if stack.empty():
                print('+')
                stack.clear()
            else:
                print('-')
                stack.clear()
