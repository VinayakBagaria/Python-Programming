test=int(input())
i=test
while i>0:
    i-=1

    n=int(input())

    k=1
    count=1
    sum=0
    while sum<n:
        k+=9
        sum=sum+k
        count+=1
    print(count)
