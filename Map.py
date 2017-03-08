def sqr(x):
    return x*x
print(list(map(sqr,[1,2,3])))
print(list(map(lambda x:x+1,[1,2,3])))

a=[1,2,3]
b=[5,6,7]
print(list(map(lambda x,y:x+y,a,b)))

n=456
print(n+int(str(n)[::-1]))