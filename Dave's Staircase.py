"""
Davis has staircases in his house and he likes to climb each staircase 1,2, or 3 steps at a time. Being a very precocious child, he
wonders how many ways there are to reach the top of the staircase.
Given the respective heights for each of the staircases in his house, find and print the number of ways he can climb each staircase
on a new line.
"""

steps={1:1,2:2,3:4}

def ways(n):
    if n not in steps.keys():
        steps[n]=ways(n-1)+ways(n-2)+ways(n-3)
    return steps[n]

test=int(input())

for i in range(test):
    print(ways(int(input())))