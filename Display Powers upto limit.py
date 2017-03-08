terms = int(input("How many terms? "))
base=int(input('Base? '))

result = list(map(lambda x: base ** x, range(terms+1)))

k=0
for i in result:
    print(base,' powered ',k,' is ',i)
    k=k+1