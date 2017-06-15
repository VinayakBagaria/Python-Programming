test=int(input())
for x in range(test):
    integer=int(input())
    binary=bin(integer)

    length=len(binary)

    aCount=0
    for i in range(2,length):
        if binary[i]=='0':
            aCount+=pow(2,length-i-1)

    if integer==0:
        print(0)
    else:
        print(aCount)