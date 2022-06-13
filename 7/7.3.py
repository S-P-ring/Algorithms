d={}
slovo=str(input())
a=int(input())
k=1
lich=0
count=0
for i in range(a):
    i=str(input())
    d[k]=i
    k+=1


for l in range(1,k):
    potoch=d[l]
    for n in potoch:
        if n in slovo and potoch.count(n)<=slovo.count(n):
            lich+=1
            

    if lich == len(potoch) :
        count+=1
        lich=0
    else:
        lich=0

print(count)

