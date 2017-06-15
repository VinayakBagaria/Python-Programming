"""
i i%4==0
1 i%4==1
i+1 i%4==2
0  i%4==3
"""

def get(k):
    seq=[k,k,2,2,k+2,k+2,0,0]
    return seq[k%8]

for i in range(int(input())):
    a,b=input().split(' ')
    a,b=[int(a),int(b)]

    print(get(a-1)^get(b))