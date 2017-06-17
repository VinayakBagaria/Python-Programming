from itertools import combinations

size=int(input())
seq=[x for x in input().split(' ')]
k=int(input())

combos=list(combinations(seq,k))

count=0
for x in combos:
    if 'a' in x:
        count+=1

print(round(count/len(combos),4))