test=int(input())

for i in range(test):
    primes = []
    primes.append(2)
    upperLimit=int(input())
    counter=1
    while len(primes)<upperLimit:
        counter+=2
        j=0
        isPrime=True

        while(primes[j]*primes[j]<=counter):
            if(counter%primes[j]==0):
                isPrime=not(isPrime)
                break
            j+=1

        if isPrime:
            primes.append(counter)

    print(primes[upperLimit-1])