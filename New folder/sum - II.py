import math
def factors(x):
    sum=0
    for i in range(2,math.sqrt(x)+1):
        if x%i == 0:
    	    if(i==x/i):
              sum+=i
            else:
    	        sum+=i+(x/i)
    return sum


test=int(input())
for j in range(0,test):
    n,k=[int(x) for x  in input().split(' ')]
    count=0
    ans=0
    for i in range(1,n+1):
        if(i**k==1):
            count=1
        else:
           count=factors(i**k)
        ans+=count
        print('{} -- {}'.format(i**k,count))
    print(ans%((10**9)+7))