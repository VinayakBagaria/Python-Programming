from itertools import product

k,m=input().split(' ')
k,m=[int(k),int(m)]

initial=[0]*k

for i in range(k):
    a = [int(x) for x in input().strip().split(' ')]
    del a[0]
    initial[i]=a

answer=list(product(*initial))
maximum=0

for x in answer:

    total=sum(a * a for a in x) % m

    if total>maximum:
        maximum=total

print(maximum)
