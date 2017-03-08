n=int(input().strip())

arr=[int(x) for x in input().strip().split(' ')]
arr=sorted(arr)

minimum=abs(arr[0])

for i in range(1,len(arr)):
    if(abs(arr[i]-arr[i-1])<minimum):
        minimum=abs(arr[i]-arr[i-1])

print(minimum)