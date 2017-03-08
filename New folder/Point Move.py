def hcf(a,b):
    while b!=0:
        rem=a%b
        a=b
        b=rem
    return a

test=int(input())
store=[None]*test
for j in range(0,test):
    line = input()
    x = line.split(' ')

    x1=int(x[0])
    x2=int(x[1])
    y1=int(x[2])
    y2=int(x[3])

    if hcf(x1,x2)==hcf(y1,y2):
        store[j]=1
    else:
        store[j]=0

for i in range(0,test):
    if store[i]==0:
        print('NO')
    else:
        print('YES')
