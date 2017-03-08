test=int(input())
list=[]*test
for i in range(0,test):
    line=input()
    x=line.split(' ')
    reverse1=int(x[0][::-1])
    reverse2=int(x[1][::-1])
    sum=reverse1+reverse2
    sum_res=int(str(sum)[::-1])
    list.append(sum_res)
for a in list:
    print(a)