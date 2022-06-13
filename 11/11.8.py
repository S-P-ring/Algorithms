n, k = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    t = lst[i]
    for j in range(i, n):
        if t > lst[j] + k:
            count += 1

print(count)