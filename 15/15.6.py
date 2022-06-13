class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


def push(head_ref, new_data):

  new_node = Node(new_data)
  new_node.data = new_data
  new_node.next = (head_ref)

  (head_ref) = new_node

  return head_ref


def printList(node):
  answer = []
  while (node != None):
    answer.append(node.data)
    node = node.next
  return answer


def rightRotate(head, k):
  if (not head):
    return head

  tmp = head
  len = 1

  while (tmp.next != None):
    tmp = tmp.next
    len += 1

  if (k > len):
    k = k % len

  k = len - k

  if (k == 0 or k == len):
    return head

  current = head
  cnt = 1

  while (cnt < k and current != None):
    current = current.next
    cnt += 1

  if (current == None):
    return head

  kthnode = current
  tmp.next = head
  head = kthnode.next
  kthnode.next = None

  return head


if __name__ == '__main__':
    counter = 0
    head = None
    with open('input.txt') as file :
        for line in file:
            if counter == 0:
                n = int(line)
            elif counter == 1:
                arr = [int(x) for x in line.split()]
                for i in arr[::-1]:
                    head = push(head, i)
            else:
                line1 = line.strip()
                if line1 != None:
                    lst1 = rightRotate(head,int(line1))
                    print(*printList(lst1))
                    head = lst1
            counter+=1
