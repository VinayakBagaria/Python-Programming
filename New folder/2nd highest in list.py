n=int(input())
l=list(map(int,input().split(' ')))
m=sm=-1000
for i in l:
    if(i>m):
        sm,m=m,i
    if(i<m and i>sm):
        sm=i
print(sm)