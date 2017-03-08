import math
test=int(input())
arr=[None]*test
for i in range(0,test):
    arr[i]=int(input())
for i in range(0,test):
    sq=1+(8*arr[i])
    root=int(math.sqrt(sq))
    if root*root==sq:
        x=(-1+root)//2
        print('Go On Bob',x)
    else:
        print('Better Luck Next Time')