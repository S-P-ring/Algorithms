class Queue:

    def __init__(self):
        self.items = []

    def front(self):
        return self.items[0]

    def push_back(self, n):
        self.items.append(n)
        return ""

    def pop_front(self):
        self.items.pop(0)
        return ""

    def empty(self):
        if len(self.items) == 0:
            return True
        return False


if __name__ == '__main__':
    n = int(input())
    igr_1 = [int(x) for x in input().split()]
    igr_2 = [int(x) for x in input().split()]

    plr_1 = Queue()
    plr_2 = Queue()

    for i in range(len(igr_1)):
        plr_1.push_back(igr_1[i])
        plr_2.push_back(igr_2[i])

    for i in range(1, 2 * 10 ** 5):
        if plr_1.front() < plr_2.front():
            plr_2.push_back(plr_1.front())
            plr_2.push_back(plr_2.front())
            plr_1.pop_front()
            plr_2.pop_front()

        elif plr_1.front() == 0 and plr_2.front() == n - 1:
            plr_1.push_back(plr_1.front())
            plr_1.push_back(plr_2.front())
            plr_1.pop_front()
            plr_2.pop_front()

        elif plr_2.front() == 0 and plr_1.front() == n - 1:
            plr_2.push_back(plr_1.front())
            plr_2.push_back(plr_2.front())
            plr_1.pop_front()
            plr_2.pop_front()
        else:
            plr_1.push_back(plr_1.front())
            plr_1.push_back(plr_2.front())
            plr_1.pop_front()
            plr_2.pop_front()

        if plr_1.empty() == True:
            print("second {}".format(i))
            break

        if plr_2.empty() == True:
            print("first {}".format(i))
            break

    if plr_1.empty() == False and plr_2.empty() == False:
        print("draw")