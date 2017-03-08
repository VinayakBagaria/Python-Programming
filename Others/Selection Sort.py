def func():
    for i in range(len(arr)-1):
        pos=i
        for j in range(i+1,len(arr)):
            if arr[pos]>arr[j]:
                pos=j
        temp=arr[pos]
        arr[pos]=arr[i]
        arr[i]=temp

arr=[2,-1,0,8,7]
func()
print(arr)