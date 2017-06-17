test=int(input())

for x in range(test):
    size=int(input())
    arr=[int(a) for a in input().split(' ')]

    if size%2==0:
        print(0)
    else:
        count=0
        for i in range(0,len(arr),2):
            count=count^arr[i]

        print(count)