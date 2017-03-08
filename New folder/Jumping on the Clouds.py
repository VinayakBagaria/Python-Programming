n=int(input())
arr=[int(x) for x in input().split(' ')]
ans,i=0,0

while i<n-1:
    if i+2>=n or arr[i+2]==1:
        i+=1
    else:
        i+=2
    ans+=1
print(ans)
