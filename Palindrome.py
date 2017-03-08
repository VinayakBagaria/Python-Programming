n=int(input())

for i in range(0,n):
    inp=input()
    rev_inp=reversed(inp)

    if(list(inp)==list(rev_inp)):
        if(len(inp)%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')