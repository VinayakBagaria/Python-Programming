n,d=[int(x) for x in input().split(' ')]
arr=[int(x) for x in input().split(' ')]

d%=n

arr2=[0]*n

for i in range(0,n):
    if(i-d<0):
        x=abs(i-d)
        arr2[n-x]=arr[i]
    else:
        arr2[i-d]=arr[i]

for x in arr2:
    print(x,end=' ')