test=int(input())

names={}

for i in range(test):
    k,v=[x for x in input().split(' ')]
    names[k]=v

for i in range(test):
    string=input()

    if string in names:
        print("{}={}".format(string,names.get(string)))
    else:
        print('Not found')