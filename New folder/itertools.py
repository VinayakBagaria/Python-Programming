from itertools import *

# Product
print('Product---')

print(list(product([1,2,3],repeat = 2)))
print(list(product([1,2,3],[3,4,5])))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))

# Permutations
print('Permutations---')

print(list(permutations([1,2,3])))
print(list(permutations([1,2,3],2)))
print(list(permutations('abc',2)))