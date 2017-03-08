i,j,k=input().strip().split(' ')
i,j,k=[int(i),int(j),int(k)]

x=[]

for i in range(i,j+1):
    diff=abs(i-int(str(i)[::-1]))

    x.append(1 if diff/k==diff//k else 0)
print(sum(x))