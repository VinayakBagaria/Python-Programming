def square_sum(lim):
    s1=0
    s2=0
    for i in range(1,lim+1):
        s1=s1+(i*i)
        s2=s2+i
    s2=s2*s2
    diff=s2-s1
    print(diff)

test=int(input())
lim=[None]*test

for i in range(0,test):
    lim[i]=int(input())

for i in range(0,test):
    square_sum(lim[i])
