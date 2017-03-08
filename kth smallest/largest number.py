n,q=input().strip().split(' ')
n,q=[int(n),int(q)]

arr=[int(x) for x in input().strip().split(' ')]

for i in range(0,q):
    x,k,type = input().strip().split(' ')
    x,k,type = [int(x), int(k), int(type)]

    store=[]

    if(type==0):
        store=[z for z in arr if z>x]
        store=sorted(store)
        index=k-1
        if len(store)<k:
            print('-1')
        else:
            print(store[index])
    else:
        store = [z for z in arr if z < x]
        store = sorted(store)
        index = len(store) - k
        if len(store)<k:
            print('-1')
        else:
            print(store[index])
