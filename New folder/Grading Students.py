n=int(input())
for i in range(0,n):
    marks=int(input())
    if(marks>=38):
        div=marks//5
        if((div+1)*5-marks<3):
            print((div+1)*5)
        else:
            print(marks)
    else:
        print(marks)