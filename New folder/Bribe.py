test=int(input())
for i in range(0,test):
    x=int(input())
    arr=[int(value) for value in input().split(' ')]
    diff=0
    for j in range(0,x-1):
        for k in range(j+1,x):
            if(arr[j]>arr[k]):
                diff+=1
    print(diff)