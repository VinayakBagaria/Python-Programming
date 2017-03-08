def hcf(a,b):
    while b!=0:
        rem=a%b
        a=b
        b=rem
    return a

test=int(input())
store=[None]*test
list=[None]*4
for j in range(0,test):
    line = input()
    x = line.split(' ')

    x1=int(x[0])
    x2=int(x[1])

    gcd=hcf(x1,x2)

    store[j]=x1*x2//(gcd*gcd)

for i in range(0,test):
    print(store[i])