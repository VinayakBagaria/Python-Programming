def isPalindrome(number):
    return str(number) == str(number)[::-1]

test=int(input())

for i in range(test):

    first=int(input())

    factors=[0,0]
    found=False

    while(not found):

        while not isPalindrome(first):
            first-=1

        palin = first
        first-=1

        for i in range(999,99,-1):
            if ((palin//i) >999 or (i*i<palin)):
                break

            if(palin%i==0):
                found=True
                factors[0]=i
                factors[1]=palin//i
                break

    print(palin)