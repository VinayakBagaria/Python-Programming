from collections import Counter

n=int(input())

types=[int(x) for x in input().strip().split(' ')]

count=Counter(types)
c=min(count.values())

x=count.most_common(c)

print(x[0][0])

