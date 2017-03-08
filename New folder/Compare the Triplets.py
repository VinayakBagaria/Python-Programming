a0,a1,a2=input().split(' ')
a0,a1,a2=int(a0),int(a1),int(a2)
b0,b1,b2=input().split(' ')
b0,b1,b2=int(b0),int(b1),int(b2)

first=0
second=0

if a0>b0:
    first+=1
if a0<b0:
    second+=1

if a1>b1:
    first+=1
if a1<b1:
    second+=1

if a2>b2:
    first+=1
if a2<b2:
    second+=1

print('{} {}'.format(first,second))