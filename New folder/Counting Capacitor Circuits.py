from math import factorial as f

n=int(input())

d=0
for i in range(1,n+1):
    d+=f(n)//(f(n-i)*f(i))

print(d)