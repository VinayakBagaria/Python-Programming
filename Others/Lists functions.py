def cube(x):
    return x*x*x

print(list(map(cube,range(1,4))))



    
def func(x,y):
    return x+y

l1=[1,2,3,4]
l2=[5,6,7,8]
l3=list(map(func,l1,l2))
print(l3)