import math
test=int(input())
store=[0]*test
for i in range(0,test):
    line=input()
    x=line.split(' ')
    start=int(x[0])
    end=int(x[1])

    store[i]=math.floor(math.sqrt(end))-math.ceil(math.sqrt(start))+1
for j in range(0,test):
    print(store[j])
