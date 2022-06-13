num1 = int(input(''))
num1 = bin(num1)
num1 = num1[2:]
max2 = int(num1, 2)
for i in num1:
    num2 = num1[0:1]
    num1 = num1[1:] + num2
    max1 = int(num1, 2)
    if max1 > max2:
        max2 = max1
print(max2)
