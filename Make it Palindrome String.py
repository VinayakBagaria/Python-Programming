test=int(input())
list=[None]*test
for i in range(0,test):
    list[i]=input()
for i in range(0,test):
    st=list[i]
    if st[::-1]==st:
        print('-1')
    else:
        for j in range(0,len(st)):
            new_str=st[0:j]+st[j+1:len(st)]
            if new_str[::-1]==new_str:
                print(j)
                break