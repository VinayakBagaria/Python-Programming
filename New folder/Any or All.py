n=int(input())

arr=[x for x in input().strip().split(' ')]

print(all([int(x)>0 for x in arr]) and any([x==x[::-1] for x in arr]))