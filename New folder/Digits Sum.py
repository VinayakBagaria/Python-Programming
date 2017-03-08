num=23
s=0
while num>0:
    rem=num%10
    s=s+rem
    num=int(num/10)
print(s)