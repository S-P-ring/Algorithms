def bin_find(value, a):
    low = 0
    mid = len(a) // 2
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    counter1 = 0
    while a[mid - counter1] == a[mid]:
        if mid - counter1 >= 0:
            counter1 += 1
        else:
            break
    counter2 = 0
    k = len(a) - mid
    for i in range(0, k):
        if a[mid + counter2] == a[mid]:
            counter2 += 1
    counter = counter1 + counter2 - 1
    if value > a[mid]:
        counter = 0
    print(counter)


colors = input()
arr_colors = input().split()
arr_colors = list(map(lambda x: int(x), arr_colors))

zap = input()
arr_zap = input().split()
arr_zap = list(map(lambda x: int(x), arr_zap))

for i in arr_zap:
    bin_find(i, arr_colors)
