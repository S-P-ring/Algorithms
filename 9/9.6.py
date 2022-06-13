def insertion_sort(array, n):
    k = 0
    for index in range(1, n):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
                k += 1
            else:
                break
            position -= 1
        array[position] = currentValue
    print(k)


chisla = []
while True:
    a = int(input())
    chisla2 = []
    if a == 0:
        break
    for i in range(0, a):
        b = int(input())
        chisla2.append(b)
    chisla.append(chisla2)

for m in range(0, len(chisla)):
    h = len(chisla[m])
    insertion_sort(chisla[m], h)
