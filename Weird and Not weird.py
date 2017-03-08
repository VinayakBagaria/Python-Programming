n=int(input())
if n%2==0:
    str='Weird'
else:
    str='Not Weird'
if n>=2 and n<=5 and n%2==0:
    str='Not Weird'
if n>=6 and n<=20 and n%2==0:
    str='Weird'
if n>20 and n%2==0:
    str='Not Weird'
print(str)
