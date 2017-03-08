import collections

test=int(input())

for i in range(0,test):
    string=input()

    if(len(string)%2!=0):
        print('-1')
    else:
        string=list(string)
        s1=str(string[0:len(string)//2])
        s2=str(string[len(string)//2:len(string)])
        x=collections.Counter(s1)-collections.Counter(s2)
        print(sum(x.values()))