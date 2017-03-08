apm=input()
hour=int(apm[0:2])
min=apm[3:5]
sec=apm[6:8]
time=apm[8:]

if(hour<10):
    h='0'+str(hour)

if time=='PM' and hour==12:
    hour=12
    h=str(hour)
if time=='PM' and hour!=12:
    hour=hour+12
    h=str(hour)
if time=='AM' and hour==12:
    h='00'

print('{}:{}:{}'.format(h,min,sec))