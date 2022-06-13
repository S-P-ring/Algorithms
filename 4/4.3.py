def binary_continuous(c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if m ** 3 + m + 1 < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    print(l)


binary_continuous(5, 0, 10)
