def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        a = len(lefthalf)
        b = len(righthalf)
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < a and j < b:
            if lefthalf[i][0] > righthalf[j][0]:
                array[k] = righthalf[j]
                j += 1
            else:
                array[k] = lefthalf[i]
                i += 1
            k += 1
        while j < b:
            array[k] = righthalf[j]
            j += 1
            k += 1
        while i < a:
            array[k] = lefthalf[i]
            i += 1
            k += 1
        return (array)


n = int(input())
robot = []
for i in range(0, n):
    nk = [int(x) for x in input().split()]
    robot.append(nk)

robot = merge_sort(robot)

for j in range(0, n):
    print("{} {}".format(robot[j][0], robot[j][1]))
    j += 1
