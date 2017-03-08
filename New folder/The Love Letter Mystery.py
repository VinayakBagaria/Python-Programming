test=int(input())

for i in range(test):
    string=input()
    s=0
    for j in range(len(string)//2):
        x=ord(string[j])-ord(string[len(string)-j-1])
        s+=abs(x)
    print(s)