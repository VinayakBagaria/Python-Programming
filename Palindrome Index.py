test=int(input())

for i in range(test):
    string=input()

    if(list(string)==list(string[::-1])):
        print('-1')
        continue

    x=len(string)

    for j in range(0,x):

        if(string[j]!=string[x-j-1]):
            s=string[0:j]+string[j+1:x]

            if(s==s[::-1]):
                print(j)
            else:
                print(x-j-1)
            break