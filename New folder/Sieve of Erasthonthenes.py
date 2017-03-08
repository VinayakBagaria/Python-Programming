n=int(input())
list=[1]*(n+1)
list[0]=0
list[1]=0

for i in range(2,n+1):
    if list[i]==1:
      j=i*2
      while j<n:
         list[j]=0
         j=j+i

for k in range(0,n):
    if list[k]==1:
        print(k)

print(n-1)
