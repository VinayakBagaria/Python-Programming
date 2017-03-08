import collections

test=int(input())

for i in range(0,test):
    string=input()
    x=collections.Counter(string)
    print(len(x.keys()))