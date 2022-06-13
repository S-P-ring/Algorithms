class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" ")
        ptr = ptr.next


def reverse(head):
    result = None
    current = head

    while current:
        next = current.next
        current.next = result
        result = current
        current = next

    return result


def shuffleMerge(a, b):
    if a is None:
        return b

    if b is None:
        return a

    recur = shuffleMerge(a.next, b.next)
    result = a
    a.next = b
    b.next = recur

    return result


def findMiddle(head):
    prev = None
    slow = fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if fast and fast.next is None:
        prev = slow
        slow = slow.next

    prev.next = None

    return slow


def rearrange(head):
    if head is None:
        return

    mid = findMiddle(head)
    mid = reverse(mid)
    shuffleMerge(head, mid)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()][::-1]
    head = None
    for i in arr:
        head = Node(i, head)

    rearrange(head)
    printList(head)