"""
2 3 8/3  11/4 19/7 87/32 193/71 1264/465 1457/536
Find the sum of the digits of the nth convergent
"""

n=int(input())
k1=2
k2=3

if n==1:
    print('2')
elif n==2:
    print('3')

else:
    n+=1
    for i in range(3,n):
        if(i%3==0):
            ans = 2*(i//3) * k2 + k1
        else:
            ans=k2 + k1

        k1 = k2
        k2=ans

    print(sum([int(x) for x in str(ans)]))