from itertools import permutations

string,number=input().split(' ')

number=int(number)

arranged=sorted(list(permutations(string,number)))

for x in arranged:
    for i in x:
        print(i,end='')
    print('')

