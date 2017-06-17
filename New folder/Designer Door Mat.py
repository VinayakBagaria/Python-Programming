n,m=input().split(' ')
n,m=[int(n),int(m)]

combo=[]

for x in range(1,n,2):
    value=((m-(3*x))//2)
    combo.append(x)
    for j in range(value):
        print('-',end='')

    for j in range(x):
        print('.|.',end='')


    for j in range(value):
        print('-', end='')

    print('')

for x in range((m-7)//2):
    print('-',end='')

print('WELCOME',end='')

for x in range((m-7)//2):
    print('-',end='')

combo=sorted(combo,reverse=True)
print(end='\n')
for x in combo:
    value=(m-(3*x))//2
    for j in range(value):
        print('-',end='')

    for j in range(x):
        print('.|.',end='')

    for j in range(value):
        print('-', end='')

    print('')

