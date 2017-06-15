size=int(input())

arr11=[int(x) for x in input().split(' ')]
arr22=[int(x) for x in input().split(' ')]

arr1=sorted(arr11)
arr2=sorted(arr22)

min1=arr1[0]
min2=arr1[1]

minA=arr2[0]
minB=arr2[1]

if arr11.index(min1)!=arr22.index(minA):
    print(min1+minA)

else:

    sum1=min1+minB
    sum2=min2+minA

    sum3=arr1[size-1]+arr2[size-1]
    if arr11.index(min2)!=arr22.index(minB):
        sum3=min2+minB

    print(min(sum1,sum2,sum3))