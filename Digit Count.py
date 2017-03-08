n=int(input())
for i in range(2,10):
    x=pow(i,n)
    s=str(x)
    if len(s)==n:
        print(s)