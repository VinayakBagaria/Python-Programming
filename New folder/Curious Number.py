def fact(a):
    prod=1
    for i in range(1,a+1):
        prod=prod*i
    return prod

def sum(count):
    s=0
    while count>0:
        rem=count%10
        f=fact(rem)
        s=s+f
        count=int(count/10)
    return s

def eval(count):
    if sum(count)%count==0:
        return (count)
    else:
        return 0


lim=int(input())
s=0
for i in range (11,lim+1):
    ans=eval(i)
    s=s+ans
    i=i+1
print(s)