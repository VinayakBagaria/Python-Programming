date=int(input())

values=[31,31,30,31,30,31,31,30,31,30,31]
if date<=1917:
    # Julian Calendar
    if date%4==0:
        feb=29
    else:
        feb=28

elif date>=1919:
    # Georgian Calendar
    if date%400==0 or (date%4==0 and date%100!=0):
        feb=29
    else:
        feb=28

else:
    feb=15


count=feb

for i in range(len(values)):
    sumDate=values[i]+count
    if sumDate>256:
        print('{}.0{}.{}'.format(256-count,i+2,date))
        break
    else:
        count+=values[i]