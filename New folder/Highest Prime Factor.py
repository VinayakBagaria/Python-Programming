#Largest Prime Factor
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return -1
    return 1

def calc_prime(n):
    p=2
    while p*p<=n:
        if (n%p==0 and prime(p)!=-1):
            n=n//p
        else:
            p=p+1
    print(n)

global take
test=int(input())
list=[None]*test
for i in range(0,test):
    list[i]=int(input())

for i in range(0,test):
    calc_prime(list[i])

