#Least Number divisible by every number from 1 to N

def LCM(a,b):
     x=a
     y=b
     while(b!=0):
         r=a%b
         a=b
         b=r
     lcm=int((x*y)/a)
     return lcm

test=int(input())
list=[None]*test
for i in range(0,test):
    list[i]=int(input())
for i in range(0,test):
    temp=1
    for j in range(2,list[i]+1):
        temp=LCM(temp,j)
    print(temp)