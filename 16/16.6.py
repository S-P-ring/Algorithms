class Node:
    def __init__(self):
        self.surroundings = {}

def find_route(first_node):
    was_here = set()
    index = 1
    queue = [n for n in first_node.surroundings if first_node.surroundings[n] == s[0]]
    while index < len(s):
        new_queue = []
        for j, node in enumerate(queue):
            was_here.add(node)
            new = [n for n in node.surroundings if node.surroundings[n] == s[index]
                   and n not in was_here]
            new_queue += new
            if index == len(s) - 1 and new_queue:
                return new_queue[0]
        index += 1
        queue = new_queue
    return None

if __name__ == "__main__":
    s = input()
    n = int(input())
    nodes = [Node() for _ in range(n)]
    first = set()
    for _ in range(n - 1):
        u, v, c = input().split()
        u, v = int(u) - 1, int(v) - 1
        if c == s[0]:
            first.add(nodes[v])
            first.add(nodes[u])
        nodes[v].surroundings[nodes[u]] = c
        nodes[u].surroundings[nodes[v]] = c
    for node in first:
        last = find_route(node)
        if last:
            print("YES")
            print(nodes.index(last) + 1, nodes.index(node) + 1)
            break
    else:
        print("NO")
