def computSum(number):
    x=sum([int(digit)**2 for digit in str(number)])
    return x

n=int(input())
sum_all=0
for i in range(1,n+1):
    get_sq=computSum(i)
    if(pow(get_sq,0.5)==int(pow(get_sq,0.5))):
        sum_all+=i
print(sum_all%(pow(10,9)+7))