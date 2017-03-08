alphas=dict((chr(96+i),i) for i in range(1,27))

newDict=dict()

string=input()
test=int(input())
strSet=set(string)

for x in strSet:
    countX = string.count(x)
    newDict[x]=countX

for i in range(test):
    n=int(input())
    flag=0

    for x in strSet:
        countX=newDict[x]
        if(countX*alphas.get(x)==n):
            print("Yes")
            flag=1
            break

        for k in range(1,countX):
            if(k*alphas.get(x)==n):
                print("Yes")
                flag=1
                break

    if(flag==0):
        print('No')


