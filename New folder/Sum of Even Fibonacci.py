def fibonacci_iter(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

test=int(input())
while test>0:
    print(sum(a for a in fibonacci_iter(int(input())) if not (a & 1)))
    test-=1

