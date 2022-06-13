from math import floor


def bin_find(arr, k):
    l = 1
    r = sum(arr) / k
    while l <= r:
        m = (r + l) // 2
        g = 0
        for i in range(len(arr)):
            g = g + floor(arr[i] / m)
        if g > k - 1:
            l = m + 1
        else:
            r = m - 1
    print(int(r))


nk = [int(x) for x in input().split()]
rows = []
for i in range(0, nk[0]):
    a = int(input())
    rows.append(a)
bin_find(rows, nk[1])
