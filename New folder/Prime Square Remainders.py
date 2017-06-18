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


test=int(input())

for x in range(test):
    limit=int(input())
    r=i=0
    val=1
    while r<limit:
        i+=2
        val+=1

        while 1:
            if is_prime(val):
                break
            val+=1

        r=2*val*i

    print(i)