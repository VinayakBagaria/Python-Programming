ad,am,ay=[int(x) for x in input().split(' ')]
ed,em,ey=[int(x) for x in input().split(' ')]

if(((ad-ed)<=0 and am==em and ay==ey) or (am<em and ay<=ey) or ay<ey):
    fine=0
else:
    if ((ad - ed) > 0 and am == em and ay == ey):
        fine=15*(ad-ed)
    elif (am > em and ay == ey):
        fine=500*(am-em)
    else:
        fine=10000

print(fine)

"""
1 1 2010
31 12 2009  - 10000

31 12 2009
1 1 2010     - 0
"""