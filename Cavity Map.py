map_array=[]
n=int(input())
for i in range(0,n):
    string=input()
    map_array.append([])
    j=0
    for s in string:
        map_array[i].append(s)

def calc():
    for i in range(0,n):
        j=0
        for j in range(0,n):
            val=int(map_array[i][j])
            if((j!=0 and j!=n-1)and(i!=0 and i!=n-1)):
                prev=int(map_array[i][j-1])
                next=int(map_array[i][j+1])
                up=int(map_array[i-1][j])
                down=int(map_array[i+1][j])
                if(val>prev and val>next and val>up and val>down):
                    print('X',end='')
                else:
                    print(val,end='')
            else:
                print(val,end='')
        print('')

calc()