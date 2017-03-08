'''
Samu had come up with new type of numbers, she named them Special Coprime numbers. Special Coprime numbers follow a property : A number N
is said to be Special Coprime if sum of its digits as well as the sum of the squares of its digits are coprime to each other.
'''

def coprime(x,y):
    while(y!=0):
        z=x%y
        x,y=y,z
    return x

def find(a,b):
    k=0
    for i in range(a,b+1):
        flag,nsum,ssum =i,0,0
        while (flag!=0):
            rem=flag%10
            nsum=nsum+rem
            ssum=ssum+(rem*rem)
            flag=flag//10
        if (coprime(ssum,nsum)==1):
            list.append(i)
            k=k+1
    count.append(k)

test=int(input())
list=[0]*test
count=[0]*test
for i in range(0,test):
    x=input().split(' ')
    ll=int(x[0])
    ul=int(x[1])
    find(ll,ul)
del list[0]
del count[0]
#for a in count:
  #  print(a,end=' ')
print(count)