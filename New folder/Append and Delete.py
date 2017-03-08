str1=input()
str2=input()
n=int(input())

if(str1==str2):
    print('Yes')
elif (set(str1)==set(str2)):
    print('Yes')
else:
    get=0
    if(len(str1)>len(str2)):
        for i in range(0,len(str2)):
            if(str1[i]!=str2[i]):
                get=i
                break
    diff_len=len(str1)-get+len(str2)-get
    print(('Yes' if diff_len<=n else 'No'))