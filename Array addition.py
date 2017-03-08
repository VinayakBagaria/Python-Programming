n=int(input())
arr1=[int(x) for x in input().split(' ')]
arr2=[int(x) for x in input().split(' ')]

for i in range(0,n,1):
    print(arr1[i]+arr2[i],end=' ')
