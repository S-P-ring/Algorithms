class Stack:

    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        self.items.pop()

    def empty(self):
        if len(self.items) == 0:
            return True
        return False


def bracket_check(bracket_arr):
    stack = Stack()
    for bracket in bracket_arr:
        if bracket == '(':
            stack.push(bracket)
        else:
            if stack.empty():
                return False
            else:
                stack.pop()

    return stack.empty()


brackets = input()
counter = 0
for i in range(0, len(brackets)):
    if brackets[i] == ')':
        continue
    ans = brackets[i:] + brackets[:i]
    if ans[-1] != '(':
        if bracket_check(list(ans)):
            counter += 1

print(counter)
