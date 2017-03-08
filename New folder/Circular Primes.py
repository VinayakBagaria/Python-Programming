# sieve of eratosthenes which returns a list, where listp[number]=1 if prime else 0
def sieve(n):
    listp = [1] * (n+1)
    listp[0] = 0
    listp[1] = 0

    for i in range(2, n+1):
        if listp[i] == 1:
            j = i * 2
            while j < n:
                listp[j] = 0
                j = j + i

    return listp

# rotate a number
def rotate(l, n):
    return l[n:] + l[:n]

# List to number conversion
def list2Num(lnumbers):
    digits = ''.join(str(n) for n in lnumbers)
    return int(digits)

# number to list conversion
def num2List(num):
    list_num = [int(d) for d in str(num)]
    return list_num


# returns the rotated primes
def generate_rotations(n):
    rotatedPrimes=[]
    list_num=num2List(n)

    for i in range(0,len(list_num)):
        rotated=list2Num(rotate(list_num,i))

        if (primes[rotated]==1):
            rotatedPrimes.append(rotated)
        else:
            rotatedPrimes.clear()
            return []

    return rotatedPrimes



x=int(input())
primes=sieve(x)
circularPrime=set()

for k in range(0,len(primes)):
    if primes[k]==1 and primes[k] not in circularPrime:
        got_list=generate_rotations(k)

        length=len(got_list)
        if(length!=0):
            for x in got_list:
                circularPrime.add(x)

print(sum(circularPrime))

