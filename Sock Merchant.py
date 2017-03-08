n=int(input())
arr=[int(x) for x in input().split(' ')]

pairs=[]
counted=0
for x in arr:
    if x not in pairs:
        counted+=arr.count(x)//2
        pairs.append(x)
print(counted)