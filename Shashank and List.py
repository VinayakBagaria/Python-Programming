n=int(input())
a_list=[int(x) for x in input().strip().split(' ')]

ans=1
m=10**9+7

for a in a_list:
    ans*=(1+pow(2,a,m))


print((ans-1)%m)