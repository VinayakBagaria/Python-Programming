n=int(input())

arr=[int(x) for x in input().split(' ')]

ans=0
for x in arr:
    ans=(ans | x) & ~(ans & x)

print(ans)