n,k=input().strip().split(' ')
n,k=[int(n),int(k)]

arr=[int(x) for x in input().strip().split(' ')]

energy=100

for i in range(0,len(arr),k):
    if(arr[i]==1):
        energy-=2
    energy-=1

print(energy)