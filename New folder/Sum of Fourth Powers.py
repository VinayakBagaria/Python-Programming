n=int(input())
lim=9**n*(n-1)
add=0
for i in range(10,lim):
    s=sum(pow(int(x),n) for x in str(i))
    if s==i:
        add=add+i
print(add)