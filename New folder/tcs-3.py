n=int(input())
arr=[int(x) for x in input().split(' ')]
count=0
diff=0
for i in (0,len(arr)-1):
    ans=arr[i]+3
    if(arr[i+1]>ans):
        diff=arr[i+1]-ans
        arr[i+1]=ans
    else:
        arr[i+1]=ans+diff