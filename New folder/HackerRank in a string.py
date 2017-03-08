x=int(input())
for i in range(0,x):
    string=input()

    wordTo="hackerrank"

    index=-1
    count=0

    for s in wordTo:
        try:
            index=string.index(s,index+1)
            count += 1
        except:
            pass

    if count==10:
        print('YES')
    else:
        print('NO')