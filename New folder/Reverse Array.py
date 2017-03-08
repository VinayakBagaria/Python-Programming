n=int(input())
arr=[int(x) for x in input().split(' ')]

arr=arr[::-1]

print(' '.join(str(p) for p in arr))