people=int(input())
ranks=[int(x) for x in input().split(' ')]

levels=int(input())
alice=[int(x) for x in input().split(' ')]

ranks=sorted(list(set(ranks)))
ranksRev=sorted(ranks,reverse=True)

print(ranksRev)
index=0


while index<levels:
    flag=-1
    for a in ranks:
        if alice[index]<a:
            print(ranksRev.index(a)+2)
            flag=0
            break
    if flag==-1:
        print('1')
    index+=1


"""
7
100 100 50 40 40 20 10
4
5 25 50 120
"""

"""
while index<levels:
    flag=-1
    for a in ranks:
        if alice[index]<a:
            print(ranksRev.index(a)+2)
            flag=0
            break
    if flag==-1:
        print('1')
    index+=1
"""