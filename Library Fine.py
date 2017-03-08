line = input()
date1 = line.split(' ')
line = input()
date2 = line.split(' ')
yr=int(date1[2])-int(date2[2])
mon=int(date1[1])-int(date2[1])
day=int(date1[0])-int(date2[0])
fine=0
if yr>0:
    fine=10000
elif yr<0:
    fine=0
elif mon>0:
    fine=500*mon
elif mon<0:
    fine=0
elif day>0:
    fine=15*day
else:
    fine=0
print(fine)