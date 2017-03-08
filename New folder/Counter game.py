def bits(n):
    count=0
    while(n!=0):
        n&=(n-1)
        count+=1
    return count

test=int(input())

for i in range(0,test):
    n=int(input())

    if(bits(n-1)&1):
        print('Louise')
    else:
        print('Richard')