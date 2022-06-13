def qsort(array, a, b):
    if a >= b: return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1

        while pivot < array[right]:
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    qsort(array, a, right)
    qsort(array, right + 1, b)
    return array


n = int(input())
chisla = [int(x) for x in input().split()]
qsort(chisla, 0, len(chisla) - 1)
print(" ".join(map(str, chisla)))
