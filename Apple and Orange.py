s,t=input().strip().split(' ')
s,t=[int(s),int(t)]

a,b=input().strip().split(' ')
a,b=[int(a),int(b)]

m,n=input().strip().split(' ')

apples=[int(x) for x in input().strip().split(' ')]
oranges=[int(x) for x in input().strip().split(' ')]

count_apples=0
for x in apples:
    if(x+a<=t and x+a>=s):
        count_apples+=1

count_oranges=0
for x in oranges:
    if(x+b<=t and x+b>=s):
        count_oranges+=1

print(count_apples)
print(count_oranges)