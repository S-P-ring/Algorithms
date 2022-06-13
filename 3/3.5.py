counter = 0
A = []
file = open("output.txt", "w")
with open("input.txt", "r") as f:
    for line in f:
        A.append(line.replace("\n", " "))
        counter += 1
    for i in range(0, counter, 3):
        var = 0
        a = list(map(int, A[i + 1].split()))
        b = list(map(int, A[i + 2].split()))
        for i in a:
            if i in range(b[0], b[1] + 1):
                var += 1
        file.write(str(var) + '\n')

f.close()
file.close()
