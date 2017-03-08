def computeSum(number):
    x=sum([int(digit)**2 for digit in str(number)])
    return x

all_nums=set()

n=int(input())
sum_all=set()
for i in range(1,n+1):
    if(len(list(str(i)))==1):
        sum_all.add(i % (pow(10, 9) + 7))
        continue
    if i not in sum_all:
        get_sq=computeSum(i)
        if(pow(get_sq,0.5)==int(pow(get_sq,0.5))):
            sum_all.add(i%(pow(10,9)+7))
print(sum(sum_all)%(pow(10,9)+7))
