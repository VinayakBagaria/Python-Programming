n=input()
nums=list(input())
count=0
for i in range(0,int(n)):
    if nums[i:i+3]==['0','1','0']:
        nums[i+2]='1'
        count+=1
print(count)