lim=int(input())
line=input()
arr=line.split(' ')
arr=list(map(int,arr))
zer=arr.count(0)
pos=sum(1 for x in arr if x>0)
neg=lim-zer-pos
print(pos/lim)
print(neg/lim)
print(zer/lim)
