n,k=[int(x) for x in input().split(' ')]
arr=[int(x) for x in input().split(' ')]

count=0

for i in range(n-1):
    for j in range(i+1,n):
        if((arr[i]+arr[j])%k==0):
            count+=1

print(count)