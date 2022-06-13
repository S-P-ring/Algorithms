nk = [int(x) for x in input().split()]
koord = [int(x) for x in input().split()]
l = 0
r = 10 ** 9
n = nk[0]
k = nk[1]


def check(n, m):
    stall = 1
    len = 0
    t = 1
    while t < n:
        len += koord[t] - koord[t - 1]
        t += 1
        if len >= m:
            len = 0
            stall += 1
    return (stall >= k)


while l <= r:
    m = (l + r) / 2
    if check(n, m):
        l = m + 1
    else:
        r = m
print(int(r))
