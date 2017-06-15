integer=int(input())
binary=bin(integer)

c=0
for i in range(2,len(binary)):
    if binary[i]=='0':
        c+=1

if integer==0:
    print(1)
else:
    print(pow(2,c))