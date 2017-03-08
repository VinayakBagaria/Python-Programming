arr=[int(x) for x in input().split(' ')]
n=arr[0]
k=arr[1]

notes=input()

friends=[int(x) for x in input().split(' ')]

count=0
canGet=[]

for i in range(0,len(notes)):
    if(notes[i]=='0'):
        canGet.append(i+1)

for k in canGet:
    if(k in friends):
        count+=1
        break

if(count==1):
    print('YES')
else:
    print('NO')