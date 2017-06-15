import math

numbers=[int(x) for x in input().split(' ')]
n=numbers[0]
k=numbers[1]

def isPentagonal(number):
    pen=(math.sqrt(24*number+1)+1)/6
    return pen==int(pen)

for i in range(1,n):
    pi=i*(3*i-1)//2
    pk=(i-k)*(3*(i-k)-1)//2

    if(isPentagonal(pi+pk) or isPentagonal(abs(pi-pk))):
        print(pi)
        print('----------')

