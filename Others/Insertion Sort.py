def func():
    l=len(arr)
    for i in range(1,len(arr)):
        pos=i
        cur=arr[pos]
        while(pos>0 and arr[pos-1]>cur):
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=cur

arr=[2,-1,0,8,6]
func()
print(arr)