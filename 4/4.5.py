def binary_continuous(c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if m ** 3 + 4 * m ** 2 + m - 6 < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(l)


binary_continuous(0, 0, 2)
