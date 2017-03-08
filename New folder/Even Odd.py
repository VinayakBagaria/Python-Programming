test=int(input())
line=input()
arr=[None]*test
x=line.split(' ')
for i in range(0,test):
    arr[i]=int(x[i])
times=int(input())
store=[None]*times
for i in range(0,times):
    line=input()
    y=line.split(' ')
    first=int(y[0])
    second=int(y[1])
    if first==0 and second==0:
        store[i]='Even'
    elif pow(arr[first-1],arr[second-1])%2==0:
        store[i]='Even'
    else:
        store[i]='Odd'
for j in range(0,times):
    print(store[j])

