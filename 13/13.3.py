class Stack:

    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def empty(self):
        return len(self.items) == 0

    def pop(self):
        return self.items.pop()


def get_char_digit(digit):
    if digit < 9:
        str_digit = str(digit)
    else:
        str_digit = '[{0}]'.format(digit)

    return str_digit


def convert(dec_number, base):
    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    converted = ""

    while not stack.empty():
        converted = converted + get_char_digit(stack.pop())

    return converted


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(convert(n, m))
