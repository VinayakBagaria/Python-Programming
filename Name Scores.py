test=int(input())

names=[]
for i in range(test):
    names.append(input().strip())

names=sorted(names)

test=int(input())
for i in range(test):
    oneName=input()

    add=0
    for j in range(len(oneName)):
        add+=ord(oneName[j])-64

    print(add*((names.index(oneName))+1))