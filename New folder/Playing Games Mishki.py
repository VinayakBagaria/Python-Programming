import math

def func(m):
    count=0
    while(m):
        m//=2
        count+=1
    return count

n,q=[int(x) for x in input().split(' ')]
arr=[int(x) for x in input().split(' ')]

for i in range(0,q):
    play=[int(x) for x in input().split(' ')]

    setsTaken=[]
    store=[]


    for x in play:
        print(arr[x-1])

    # count=sum([math.floor(math.log(x)/math.log(2))+1 for x in store if x!=0])
    # if store.count(0)==len(store):
    #     print('Mishki')
    #     break
    # if(count%2==1):
    #     print('Mishki')
    # else:
    #     print('Hacker')
    #
    #
