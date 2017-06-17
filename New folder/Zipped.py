n,x=input().split(' ')
n,x=[int(n),int(x)]

arr=[0]*x
for i in range(x):
    arr[i]=[float(a) for a in input().strip().split(' ')]

for j in zip(*arr):
    print(sum(a for a in j)/x)