values=[int(x) for x in input().split(' ')]
n=values[0]
rot=values[1]
q=values[2]
arr=[int(x) for x in input().split(' ')]
rot=rot%n
temp=[]
count=-1
for i in range(n-rot,n):
    temp.append(arr[i])
    count+=1
for i in range(n-rot-1,-1,-1):
    arr[i+rot]=arr[i]
for i in range(0,count+1):
    arr[i]=temp[i]
for j in range(0,q):
    print(arr[int(input())])
