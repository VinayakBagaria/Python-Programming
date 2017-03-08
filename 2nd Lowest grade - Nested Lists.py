n=int(input())
m=sm=101.0
nl=[]
for i in range(n):
    name=input()
    grade=float(input())
    if(grade<m):
        sm,m=m,grade
    if(grade>m and grade<sm):
        sm=grade
    nl.append([name,grade])
res=[]
for i in range(n):
    if(nl[i][1]==sm):
        res.append(nl[i][0])
res.sort()
print('\n'.join(str(i) for i in res))
