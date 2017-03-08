test=int(input())

for i in range(test):
    string=input()

    for j in range(0,len(string),2):
        print(string[j],end='')
    print(end=' ')
    for j in range(1, len(string), 2):
        print(string[j], end='')

    print(' ')
