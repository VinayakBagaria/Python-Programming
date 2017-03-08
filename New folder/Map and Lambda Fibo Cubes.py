n=int(input())

a=0
b=1
l=[]

for i in range(n):
    l.append(a)
    c=a+b
    a=b
    b=c

print(list(map(lambda x:x**3,l)))