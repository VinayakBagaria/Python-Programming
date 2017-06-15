n=int(input())

unsorted=[]

for x in range(n):
    unsorted.append(input())

print('\n'.join(sorted(unsorted, key=int)))