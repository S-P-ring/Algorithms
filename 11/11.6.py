def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        if [c, c + [a[0]]] not in cs:
            cs += [c, c + [a[0]]]
    return cs


def sequences(a, b, c, index):
    oc = []
    max = b - c * (a - 1)
    for j in range(0, max - c + 1):
        oc.append(j + c)
    oc_com = combs(oc * a)
    oc_com2 = []
    for k in oc_com:
        if len(k) == a:
            oc_com2.append(k)
    answer = []
    for m in oc_com2:
        if m not in answer:
            if sum(m) == b:
                answer.append(m)

    print(answer)
    print(len(answer))


m = int(input())
tests = []
for i in range(0, m):
    n, t, p = [int(x) for x in input().split()]
    sequences(n, t, p, i)
