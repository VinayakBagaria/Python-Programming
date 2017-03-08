line=input()
arr=[int(value) for value in input().split(' ')]
least=[]
for i in range(0,int(line)):
    for j in range(i,int(line)):
        if(i!=j and arr[i]==arr[j]):
            least.append(j-i)
if(len(least)==0):
    print('-1')
else:
    print(min(least))