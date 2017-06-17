from itertools import product

a=[int(x) for x in input().split(' ')]
b=[int(x) for x in input().split(' ')]

answer=sorted(list(product(a,b)))

for x in answer:
    print(x,end=' ')