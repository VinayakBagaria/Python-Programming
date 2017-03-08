import math

num=int(input())
l=[]

def isPrime(n):
    for k in range(2,math.floor(n/2)+1):
        if(n%k==0):
            return 0
    return 1

def genPrime():
    for i in range(2,num):
        if(isPrime(i)):
            l.append(i)

def sumGen():
    for j in range(2,num):
        if(l.__contains__(j) & l.__contains__(num-j)):
            print('{0} = {1} + {2}'.format(num,j,num-j))
            break

genPrime()
sumGen()