test=int(input())

for i in range(test):
    n=int(input())

    power=pow(2,n)

    sumPower=sum([int(c) for c in str(power)])

    print(sumPower)