"""
result=0    set=7,6,6,2,7 -> 111,110,110,010,111     ^-XOR
result^111=111
result^110=001
result^110=111
result^010=101
result^111=010

thus answer = 010 = 2
"""

n=int(input())
arr=[int(x) for x in input().strip().split(' ')]

set_arr=set(arr)

result=0
for x in arr:
    result=result^x

print(result)