n,k=input().strip().split(' ')
n,k=[int(n),int(k)]

cost=[int(x) for x in input().strip().split(' ')]
charged=int(input())

actual=sum(cost[x] for x in range(len(cost)) if x!=k)//2

if(actual==charged):
    print('Bon Appetit')
else:
    print(charged-actual)

