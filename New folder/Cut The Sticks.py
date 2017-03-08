n=int(input())
arr=[int(x) for x in input().split(' ')]
arr.sort()            # sort to get the lowest value in the list
while(len(arr)!=0):       # while there is some value in the list
    print(len(arr))

    mini=arr[0]           # store the lowest value
    new_arr=[]            # make a new list which stores other values
    for j in range(0,len(arr)):
        if(arr[j]>mini):  # store these values only if it is largest than the smallest value
            new_arr.append(arr[j])
    arr=new_arr