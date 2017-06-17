from itertools import combinations_with_replacement

string,k=input().split(' ')

k=int(k)
combos=list(combinations_with_replacement(sorted(string),k))

for x in combos:
    for loop in x:
        print(loop,end='')
    print('')
