line = input()
x = line.split(' ')
nodes=int(x[0])
diff=int(x[1])
points=[None]*(nodes-1)
arr=[None]*2*(nodes-1)
cp=0
count=0
for i in range(0,nodes-1):
    line = input()
    x = line.split(' ')
    arr[cp]=int(x[0])
    arr[cp+1]=int(x[1])
    cp=cp+2
j=0
done=[]
while j<cp:
    first=arr[j]
    if done.count(first)==0:
        done.append(3)
        k=j+1
        while k<cp:
            second=arr[k]
            sub=abs(second-first)
            if sub<=diff:
                count=count+1
            k=k+2
    j=j+2
print(count)