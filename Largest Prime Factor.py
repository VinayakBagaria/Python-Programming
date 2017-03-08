"""
http://www.mathsisfun.com/prime-factorization.html

Take the number, reduce and divide it by 2 until that number is no longer divisible by 2.
If it is not divisible, increase the counter by 1. Do this process until counter^2 < number.
NOTE : If the number is not divisible by 2 then it is not divisible by 4. This is how it finds the prime numbers only.

Put the counter in the set in if statement to know all the prime factors.
"""

number=int(input())

largestFact=0

counter=2

while(counter*counter<=number):
    if(number%counter==0):
        number//=counter
        largestFact=counter
    else:
        counter+=1


if(number>largestFact):
    largestFact=number

print(largestFact)
