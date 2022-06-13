def checkMinHeap(A, i):
    if 2 * i + 2 > len(A):
        return True

    left = (A[i] <= A[2 * i + 1]) and checkMinHeap(A, 2 * i + 1)

    right = (2 * i + 2 == len(A)) or (A[i] <= A[2 * i + 2]
                                      and checkMinHeap(A, 2 * i + 2))

    return left and right


if __name__ == "__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()]
    if checkMinHeap(numbers, 0):
        print('YES')
    else:
        print('NO')