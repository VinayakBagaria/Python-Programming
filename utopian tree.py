test=int(input())

for i in range(test):
    n=int(input())

    sum_powers=pow(2,(n//2)+1)-1

    if(n==0):
        print('1')
    else:
        if(n%2==0):
            print(sum_powers)
        else:
            print(sum_powers*2)
