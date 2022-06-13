class Node:

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)


class List:
    def __init__(self):

        self.head = None

    def __repr__(self):

        nodes = []
        items = self.head
        while items:
            nodes.append(repr(items))
            items = items.next
        return ' '.join(nodes)


    def append(self, item):

        if not self.head:
            self.head = Node(item)
            return
        items = self.head
        while items.next:
            items = items.next
        items.next = Node(item)


    def reverse(self):
        items = self.head
        prev_ = None
        next_ = None
        while items:
            next_ = items.next
            items.next = prev_
            prev_ = items
            items = next_
        self.head = prev_

if __name__ == '__main__':
    lst = List()

    n = int(input())
    arr = [int(x) for x in input().split()]

    for i in arr:
        lst.append(i)

    print(lst)
    lst.reverse()
    print(lst)