def func(arr,x):
    for i in range(len(arr)):
        if arr[i]==x :
            return i
    return -1

arr=[1,2,4,5,6,7]
if func(arr,5) == -1:
    print('Not there')
else:
    print('Present')