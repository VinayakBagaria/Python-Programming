line=input()
space=line.count(' ')
iterate=len(line)-space
flag=-1
list = line.split(' ')
l=len(list)
print(l)
for i in range(0,l):
    for j in range(0,l):
        if i != j:
            print('here')
            for k in range(0,len(list[i])):
                ch=list[i][k]
                if list[j].count(ch)>0:
                    flag=0
                   # break
        if flag==-1:
             print(len(list[i])*len(list[j]))
             break
        else:
            flag=-1
        flag=-1