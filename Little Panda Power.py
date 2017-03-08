test=int(input())
store=[None]*test
for j in range(0,test):
    line = input()
    x = line.split(' ')

    x1=int(x[0])
    x2=int(x[1])
    x3=int(x[2])

    if x2>0:
        store[j]=pow(x1,x2,x3)
    else:
        x2=abs(x2)
        store[j]=pow(x1,x2)
        x=str(store[j])
        l=len(x)
        store[j]=store[j]%pow(10,l)
for i in range(0,test):
    print(store[i])
