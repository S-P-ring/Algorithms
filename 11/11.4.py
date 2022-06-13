import math


def karatsuba(n, m):
    if n <= 1000 or m <= 1000:
        return n * m
    else:
        k = 10 ** int(math.log10(n) / 2.0 + 0.5)
        a, b = n // k, n % k
        c, d = m // k, m % k
        s1 = karatsuba(a, c)
        s2 = karatsuba(b, d)
        s3 = karatsuba(a + b, c + d) - s1 - s2
        return k ** 2 * s1 + k * s3 + s2


n, m = [int(n) for n in input().split()]
print(karatsuba(n, m))
