from itertools import combinations

string,k=input().split(' ')

k=int(k)

for i in range(1,k+1):
    combos=list(combinations(sorted(string),i))

    for x in combos:
        for loop in x:
            print(loop,end='')
        print('')
