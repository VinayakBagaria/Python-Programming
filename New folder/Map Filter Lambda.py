items=[1,2,3,4]
def square(i):
    return i*i
'''
    Map can be used to update all elements in a list, instead of using a for loop.
    map(function,sequence) returns applies the passed-in function to each item iterable in the sequence and returns a list containing
    the function call result.
'''
print(list(map(square,items)))