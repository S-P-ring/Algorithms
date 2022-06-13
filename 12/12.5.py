class Stack:

    def __init__(self):
        self.items = []

    def push_back(self, n):
        self.items.append(n)

    def back(self):
        return self.items[-1]

    def pop_back(self):
        self.items.pop()

    def clear(self):
        self.items.clear()

    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    while True:

        n = int(input())

        if n == 0:
            break

        while True:
            lst = [int(x) for x in input().split()]  # 5 4 3 2 1

            if lst[0] == 0:
                break

            number = lst[0]  # 5
            j = 0
            for i in range(1, n + 1):

                stack.push_back(i)  # 1 2 3 4 5
                # print(stack.empty)
                while (stack.empty() == False and number == stack.back()):  # number != 5 (1,2,3,4,5)
                    # 1 2 3 4 5
                    stack.pop_back()
                    j += 1
                    try:
                        number = lst[j]
                    except IndexError:
                        pass

            if stack.empty():
                print('Yes')
                stack.clear()
            else:
                print('No')
                stack.clear()

        print('')
