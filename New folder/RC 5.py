import math
test=int(input())
list=[None]*test
line=input()
x=line.split(' ')
for a in range(0,test):
    list[a]=int(x[a])

sum=0
for i in list:
    sum=sum+math.pow(2,i)

print(int(sum))