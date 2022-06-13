from math import sqrt


def check(c, m):
    if sqrt((c[1][0] - c[0][0]) ** 2 + (c[1][1] - c[0][1]) ** 2) < m:
        return True


k = 0
total = 0
n, mux = [int(x) for x in input().split()]
arr = []
for i in range(n):
    arr.append([int(j) for j in input().split()])

while k < len(arr):
    c = [arr[0]]
    j = 1
    for i in range(len(arr) - 1):
        c = [arr[0], arr[j]]
        if (check(c, mux)):
            total += 1
        j += 1
    arr.remove(arr[k])

print(total)
