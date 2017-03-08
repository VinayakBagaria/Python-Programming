import math

test=int(input())

for i in range(test):
    n=int(input())
    x=math.factorial(n)
    sum_ans = sum(int(digit) for digit in str(x))

    print(sum_ans)