from fractions import Fraction


test=int(input())
arr=[]
while(test>0):
    n=int(input())
    arr.append(n)
    test-=1
initial=list(arr)
arr.sort()
ans=set()
final={}

for i in range(2,arr[len(arr)-1]+1):
    for j in range(1,i):
        ans.add(str(Fraction(j,i)))
    if i in arr:
        final.update({i:len(ans)})

for a in initial:
    print(final.get(a))