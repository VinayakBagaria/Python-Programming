test=int(input())
for i in range(0,test):
    line=input().split(' ')
    minimum=int(line[1])
    arr=[int(a) for a in input().split(' ')]
    ans=sum(1 for x in arr if x<=0)
    if ans>=minimum:
        print('NO')
    else:
        print('YES')