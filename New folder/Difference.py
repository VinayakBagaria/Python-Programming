line = input()
x = line.split(' ')
lim=int(x[0])
count=0
difference=int(x[1])
line = input()
dict1={}
arr = line.split(' ')
one=[1]*lim

dict1=dict(zip(arr,one))

for i in range(0,lim):
    value=int(arr[i])-difference
    v=str(value)
    if dict1.get(v)==1:
        count=count+1
print(count)