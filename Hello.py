n=int(input())
#Dictionary
a={}
for i in range(0,n):
    s=input().split(' ')
    a[str(i)+'Name']=s[0]
    a[str(i)+'Marks1']=float(s[1])
    a[str(i)+'Marks2']=float(s[2])
    a[str(i)+'Marks3']=float(s[3])
st=input()
for i in range(0,n):
    if(a[str(i)+'Name']==st):
        avg=a[str(i)+'Marks1']+a[str(i)+'Marks2']+a[str(i)+'Marks3']
        # display 2 decimal places, even trailing 0s
        print(format(avg/3,'.2f'))
        break