string=input()
str=input()
count=0
length=len(string)-len(str)
take=len(str)

for i in range(0,length+1):
    if str==string[i:take]:
        count=count+1
    take=take+1

print(count)