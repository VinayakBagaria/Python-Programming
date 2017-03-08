n = int(input())
lsum = 0
rsum=0
for i in range(0,n):
    a=[int(x) for x in input().split(' ')]
    for j in range(0,n):
        if (i == j):
            lsum =lsum + a[j];
        if (i + j == n - 1):
            rsum =rsum + a[j];
print(abs(lsum-rsum))