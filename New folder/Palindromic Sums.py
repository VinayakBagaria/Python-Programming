test=int(input())

for i in range(test):

    limit,d=map(int,input().split(' '))

    allVals=[]

    for i in range(1,limit):
        number=i*i
        for j in range(i+d,limit,d):
            number+=(j*j)

            if number>limit:
                break

            if str(number)==str(number)[::-1] and number not in allVals:
                allVals.append(number)


    print(sum(allVals))