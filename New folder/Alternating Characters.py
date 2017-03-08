test=int(input())
for i in range(0,test):
    string=input()
    count=0
    for j in range(1,len(string)):
        if(string[j]==string[j-1]):
           count+=1
    print(count)