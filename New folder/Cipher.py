n,k=input().split(' ')
n,k=[int(n),int(k)]

k=k%n

cipherText=[int(x) for x in input()]

plainText=[100]*n

plainText[0]=cipherText[0]

for i in range(1,k):
    plainText[i]=cipherText[i-1]^cipherText[i]

plainText[n-1]=cipherText[n+k-2]

c=1
i=n+k-3

for x in range(c,n-k):
    plainText[n-x-1]=plainText[n-x]^cipherText[i]
    x-=1

for i in plainText:
    print(i,end='')