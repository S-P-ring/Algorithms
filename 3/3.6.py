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

    if low > high:
        print("NO")
    else:
        print("YES")


Koll = input()
arr_Koll = input().split()
arr_Koll = list(map(lambda x: int(x), arr_Koll))

Dizn = input()
arr_Dizn = input().split()
arr_Dizn = list(map(lambda x: int(x), arr_Dizn))

for i in arr_Dizn:
    bin_find(i, arr_Koll)
