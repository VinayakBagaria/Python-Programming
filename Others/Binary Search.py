def func(arr,ll,ul,x):
    if ll<=ul:
        mid=int((ll+ul)/2)
        print(mid)
        if arr[mid]==x:
            print('Yes')
            return
        if arr[mid]<x:
            func(arr,mid+1,ul,x)
        if arr[mid]>x:
            func(arr,ll,mid-1,x)
    else:
        print('Not there')

arr=[1,2,3,4,5]
length=len(arr)
func(arr,0,length-1,0)