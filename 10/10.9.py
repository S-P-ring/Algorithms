def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c + [a[0]]]
    return cs


def sym(m, l):
    comb_l = combs(l)
    s = []
    for j in comb_l:
        mus = sum(j)
        if mus < m:
            s.append(mus)
        elif mus == m:
            return mus
    return max(s)


answer = []
max_length = []
length_track = []
with open('input1.txt') as file:
    for line in file:
        line = [int(x) for x in line.split()]
        max_length.append(line[0])
        length_track.append(line[2:])

for i in range(0, len(max_length)):
    answer.append(sym(max_length[i], length_track[i]))

for i in answer:
    print("sum:{}".format(i))
