def is_prime(a):
    return all(a % i for i in range(2, a))

test=int(input())

for i in range(0,test):
    n=int(input())
    x=1
    count=0
    while(n-2*(x**2)>=2):
        prime=n-2*(x**2)
        if(is_prime(prime)):
            count+=1
        x+=1

    print(count)
