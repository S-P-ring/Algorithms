from math import sqrt


def binary_continuous(c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if m ** 2 + sqrt(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(l)


c = float(input())
binary_continuous(c, 1, 10 ** (10))
