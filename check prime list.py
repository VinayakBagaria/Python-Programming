x=int(input())
nums=[]
for i in range(0,x):
    nums.append(int(input()))

n=max(nums)
list=[1]*(n+1)
list[0]=0
list[1]=0

primeArray=[]

for i in range(2,n+1):
    if list[i]==1:
      j=i*2
      while j<n+1:
         list[j]=0
         j=j+i

for k in range(0,n+1):
    if list[k]==1:
        primeArray.append(k)


for i in nums:
    if(i in primeArray):
        print('Prime')
    else:
        print('Not prime')
