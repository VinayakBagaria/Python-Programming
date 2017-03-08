line=input()
space=line.count(' ')
iterate=len(line)-space

for j in range(0,iterate-1):
    list = line.split(' ')

slow=fast=0

while fast<iterate:
    slow=slow+1
    fast=fast+2
print(slow)

