number=int(input())
primeFactors=[]
for i in range(2,number+1):
    while(number%i==0):
        primeFactors.append(i)
        number=number/i
print(primeFactors)