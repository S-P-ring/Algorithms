from math import sin


def binary_continuous(c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if sin(m) - m / 3 > c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(l)


binary_continuous(0, 1.6, 3)
