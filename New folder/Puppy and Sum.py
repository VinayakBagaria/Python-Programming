test=int(input())
while test>0:
    test-=1

    arr=[int(x) for x in input().split(' ')]
    d=arr[0]
    n=arr[1]

    i=0
    sum=0
    for i in range(0,d):
        sum=(n/2)*(n+1)
        n=sum
    print(int(sum))