from sympy import *


try:
    test=int(input())
    for j in range(0,test):
        have=[]
        n,k=input().split(' ')
        n=int(n)
        k=int(k)
        for i in range(1,n+1):
            have.append(len(divisors(i**k)))

        print(sum(have)%((10**9)+7))

except Exception as ex:
    template = "An exception of type {0} occured. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)