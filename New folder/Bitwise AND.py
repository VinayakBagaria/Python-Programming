for _ in range(int(input())) :
    n, k = [int(i) for i in input().strip().split()]
    print(k-1 if (k-1)|k <= n else k-2)