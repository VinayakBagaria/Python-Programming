m=int(input())
line = input()
x = line.split(' ')
n=int(input())
str = input()
y = str.split(' ')

miss=[]
count=0

duplicates=list(set(x) & set(y))

for i in range(0,len(duplicates)):
    num1=duplicates[i]
    if x.count(num1)!=y.count(num1):
        miss.append(num1)
        count=count+1

miss.sort()

output = []
for x in miss:
    if x not in output:
        output.append(x)
        print(x,end=" ")