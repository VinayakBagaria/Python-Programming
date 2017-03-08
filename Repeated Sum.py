test=int(input())
i=test
while i>0:
    i-=1
    arr=[int(x) for x in input().split(' ')]
    d=arr[0]
    n=arr[1]

    k=1
    ans=0
    while(k<=d):
        ans=(n/2)*(2+(n-1)*1)
        n=ans
        k+=1
    print(int(ans))
