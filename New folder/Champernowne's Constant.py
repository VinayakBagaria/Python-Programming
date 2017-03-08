test=int(input())
arr=[0,0,0,0,0,0,0]
for k in range(0,test):
    prod=1
    str=input()
    s=str.split(' ')
    for i in range(0,7):
        arr[i]=int(s[i])
        if(arr[i]>=13):
            prod=prod+((arr[i]-13)*10+11)
        elif arr[i]==12:
            prod=prod*1
        else:
            prod=prod*(arr[i])
    print(prod)