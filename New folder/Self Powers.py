#showing last 10 digits

n=int(input())
s=sum(pow(x,x,10**10) for x in range(1,n+1))
div=s%10**10
print(div)
