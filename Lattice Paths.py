"""
For 2X2 grid :- DDRR, DRDR, DRRD, RDRD, RDDR, RRDD . Here there are 2 d and 2 r

for 1X3 grid :- rrrd, rrdr, .... so 1 d and 3 r

Generally, for nXm :- n downs and m rights
So how to select n downs out of n+m move in a path is a binomial co-eff.
"""


from math import factorial as f

test=int(input())

for i in range(test):
    arr = [int(x) for x in input().split(' ')]
    n = arr[0]
    m = arr[1]

    num=f(n+m)
    denom=f(n)*f(m)

    print((num//denom)%1000000007)
