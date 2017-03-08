# Finding the max number of consecutive 1s in a binary representation of a base-10 number

n=int(input())

nums=[0]*n
x=0

while(n>0):
    remainder=n%2
    n=n//2
    if(remainder==1):
        nums[x]+=1
    else:
        x+=1

print(max(nums))
