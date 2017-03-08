# Count no. of times hackerearth comes in a string

n=int(input())
string=input()

hc=string.count('h')
ac=string.count('a')
ec=string.count('e')
cc=string.count('c')
kc=string.count('k')
rc=string.count('r')
tc=string.count('t')

least=hc/2

if(ac/2<least):
    least=ac/2
if(ec/2<least):
    least=ec/2
if(cc<least):
    least=cc
if(kc<least):
    least=kc
if(rc/2<least):
    least=rc/2
if(tc<least):
    least=tc

print(int(least))