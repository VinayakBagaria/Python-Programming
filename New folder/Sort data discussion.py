n,m=map(int,input().split(' '))

arr=[[int(x) for x in input().split(' ')] for i in range(n)]

k=int(input())

arr.sort(key=lambda x:x[k])

for num in arr:
    print(*num)