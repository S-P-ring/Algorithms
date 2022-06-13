def vibor_sort(array, k):
    for i in range(0, k):
        maxpos = i
        for j in range(i + 1, k):
            if array[maxpos] > array[j]:
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]
    return (array)


n = int(input())
orcs = []
for i in range(0, n):
    a = input()
    if a.isdigit() == False:
        orcs.append(a)
array1 = vibor_sort(orcs, n)
for k in range(0, n):
    print(array1[k])
