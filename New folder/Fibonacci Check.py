def fibo(n):
    a=0
    b=1
    while a<n:
        c=a+b
        a=b
        b=c
    if a==n:
        return 1
    else:
        return 0

test=int(input())
store=[None]*test
list=[None]*4
for j in range(0,test):
    x=int(input())
    if fibo(x) == 1:
        store[j]=1
    else:
        store[j]=0


for i in range(0,test):
    if store[i] == 1:
        print("IsFibo")
    else:
        print("IsNotFibo")