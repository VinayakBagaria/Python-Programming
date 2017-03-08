test=int(input())
list=[None]*test

for i in range(0,test):
    list[i]=input()

for i in range(0,test):
    x=''.join(reversed(list[i]))
    print(x)