def stirling(n,k):
    if ((n-k) & (k-1))/2==0:
        return 1
    else:
        return 0

test=int(input())
list=[]*test
for i in range(0,test):
    line=input()
    x=line.split(' ')
    result=stirling(int(x[0]),int(x[1]))
    list.append(result)
for a in list:
    print(a)