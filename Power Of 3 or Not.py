import math

number=int(input())
#power1=math.log(number)
power2=math.log(3)
#print(math.pow(3,5))
#print(3**power1==number)
#print(power1/power2)

#print(!(number & (number-1)))
#print(bin(number).count(1)==1)

numberOfOneBits = 0;

while(number and numberOfOneBits <=1):

    if ((number & 1) == 1):
      numberOfOneBits+=1
    number >>= 1;

print(numberOfOneBits == 1)

print(number > 0 and (number & (number - 1)))