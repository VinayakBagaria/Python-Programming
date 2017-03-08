#Find Digits

test=int(input())
li=[None]*test
count=[None]*test
count=0
for i in range(0,test):
    li[i]=int(input())

def mod(x):
    count=0
    back=x
    while x>0:
        rem=x%10
        if rem != 0 and back%rem == 0:
            count=count+1
        x=x//10
    return count

l=list(map(mod,li))

for i in range(0,test):
    print(l[i])
