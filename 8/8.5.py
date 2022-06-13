def bubble_sort(array, n):
    k = 0
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                k += 1
    print(k)


num = int(input())
mass = [int(x) for x in input().split()]
bubble_sort(mass, num)
