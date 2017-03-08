import math


#number=int(input())
#print(math.fabs(math.sqrt(number))%1==0)
a=[2,3,1,5,4]
l=len(a)
def sort():
    for i in range(l-1):
        for j in range(l-i-1):
            if (a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

sort()
print(a)