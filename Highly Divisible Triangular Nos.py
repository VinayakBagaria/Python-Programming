def noOfDivisors(number):
    counter = 1
    primes=set()
    while (counter * counter <= number):
        if (number % counter == 0):
            primes.add(counter)
            primes.add(number//counter)
        counter += 1

    return len(primes)


test=int(input())

countPrime=dict()

for i in range(test):
    n=int(input())

    number=0
    i=1

    if(number in countPrime.keys()):
        print(countPrime[number])
    else:

        while noOfDivisors(number)<=n:
            number+=i
            i+=1

            countPrime[number] = noOfDivisors(number)

        print(number)