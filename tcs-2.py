import math
from math import factorial
def combination(n,k):
    numerator=factorial(n)
    denominator=(factorial(k)*factorial(n-k))
    answer=numerator/denominator
    return answer
arr=[int(x) for x in input().split(' ')]
n=arr[0]
k=arr[1]
sum=0
for i in range(0,k+1):
    if (i%2==0):
        sum=sum+combination(n,i)
print(int(sum)%(math.pow(10,9)+7))