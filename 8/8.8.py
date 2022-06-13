def insertion_sort(array, k):
    for i in range(1, k):
        currentValue = array[i]  # запам’ятовуємо елемент
        position = i  # та його позицію
        # пошук позиції для вставки поточного елемента
        while position > 0:
            if array[position - 1] > currentValue:
                # зсув елементу масиву вправо
                array[position] = array[position - 1]
            else:
                # знайдено позицію
                break
            position -= 1
        # Вставка поточного елемента у знайдену позицію
        array[position] = currentValue
    return (array)


n = int(input())
moment = []
for i in range(0, n):
    nk = [int(x) for x in input().split()]
    moment.append(nk)

moment = insertion_sort(moment, n)

for j in range(0, n):
    print("{} {} {}".format(moment[j][0], moment[j][1], moment[j][2]))
    n += 1
