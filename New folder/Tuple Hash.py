n=int(input())
# hash returns the hash value of the object(if it has one)
# tuple(x) stores the element x in a tuple
print(hash(tuple([int(i) for i in input().split(' ')])))