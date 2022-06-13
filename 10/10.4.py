import math



def count(a, b):
    koord = []
    kol = 0
    for i in range(0, a):
        x, y = map(int, input().split())
        znach = x * x + y * y
        koord.append(znach)

    for k in range(len(koord)):
        for j in range(k + 1, len(koord)):
            if math.sqrt(koord[k] + koord[j]) < b:
                kol += 1
    return kol


a, b = map(int, input().split())
print(count(a, b))
