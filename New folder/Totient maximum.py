"""
n/phi(n) = 1/PI(1-(1/p))

If the above thing has to be maximised, it will happen for the number with most distinct small prime factors.
So multiply primes until the limit is reached.
"""
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


primes=list(filter(is_prime,range(1,200)))

test=int(input())

for i in range(test):
    limit=int(input())
    result=1
    i=0

    while (result*primes[i]<limit):
        result*=primes[i]
        i+=1

    print(result)