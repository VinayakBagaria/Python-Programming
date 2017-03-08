test=int(input())
while test>0:
    test-=1
    arr=[int(x) for x in input().split(' ')]
    n=arr[0]
    m=arr[1]
    s=arr[2]
    i=1
    ans=(m+s-1)%n
    if(ans==0):
        ans=n
    print(ans)