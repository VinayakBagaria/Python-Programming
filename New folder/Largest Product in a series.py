test=int(input())
while test>0:
    test-=1

    arr=[int(x) for x in input().split(' ')]
    n=arr[0]
    k=arr[1]

    string=input()

    i=0
    pro=0
    while(i<=n-k):
        j=1
        ans=1
        series=string[i:i+k]

        for c in series:
            ans*=int(c)

        if ans>pro:
            pro=ans
        i+=1
    print(pro)