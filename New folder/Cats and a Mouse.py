q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    catA=abs(x-z)
    catB=abs(y-z)

    if catA==catB:
        print('Mouse C')
    elif catA<catB:
        print('Cat A')
    else:
        print('Cat B')