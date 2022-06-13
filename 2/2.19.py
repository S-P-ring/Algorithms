import time


def trib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    t1 = 0
    t2 = 1
    t3 = 1
    count = 3
    while count < n:
        count += 1
        temp = t3
        t3 += t2 + t1
        t1 = t2
        t2 = temp
    return t3


start_time1 = time.time()
print('T(10)=', trib(10))
print(time.time() - start_time1)
start_time2 = time.time()
print('T(20)=', trib(20))
print(time.time() - start_time2)
start_time3 = time.time()
print('T(50)=', trib(50))
print(time.time() - start_time3)
