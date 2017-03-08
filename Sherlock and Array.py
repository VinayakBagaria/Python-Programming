test=int(input())
for i in range(0,test):
    n=int(input())
    arr=[int(x) for x in input().split(' ')]

    left=0
    right=0
    while len(arr)!=1:
        l=arr[0]
        r=arr[len(arr)-1]
        if(left+l<=right+r):
            left+=l
            del arr[0]
        else:
            right+=r
            del arr[len(arr)-1]


    if(left==right):
        print('YES')
    else:
        print('NO')