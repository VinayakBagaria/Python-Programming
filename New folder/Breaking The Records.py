size=int(input())
arr=[int(x) for x in input().split(' ')]

lowest=highest=arr[0]

lCount=hCount=0

for i in range(1,size):
    if lowest<arr[i]:
        lCount+=1
        lowest=arr[i]

    if highest>arr[i]:
        hCount+=1
        highest=arr[i]


print(str(lCount)+' '+str(hCount))