def prints(x):
    new_list=[]
    for i in x:
        if i not in new_list:
            print(i,end='')
            new_list.append(i)
string=input()
k=int(input())
n=len(string)//k
parts=[string[i:i+k] for i in range(0,k*n,k)]

for x in parts:
    prints(x)
    print(' ')