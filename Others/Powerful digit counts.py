import math
n=int(input())
ll=10**(n-1)
ul=(10**n)
for i in range(ll,ul):
    root=math.floor(math.pow(i,1/n))
    if math.pow(root,n)==i:
        print(i)