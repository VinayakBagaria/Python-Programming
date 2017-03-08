test=int(input().strip())
while test>0:
    test-=1
    m=int(input().strip())
    n=int(input().strip())
    arr=[int(x) for x in input().strip().split(' ')]
    for k in range(0,n):
        newarr=arr[:k]+arr[k+1:n]
        if((m-arr[k]) in newarr):
            print(k+1,end=' ')
            if(arr.index(m-arr[k])>arr.index(arr[k])):
                print(arr.index(m-arr[k])+1)
            else:
                print(newarr.index(m-arr[k])+2)
            break