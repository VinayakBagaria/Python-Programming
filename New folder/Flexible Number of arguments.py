def add_numbers(*args):                #storing n arguments
    total=0
    for a in args:
        total+=a
    print(total)

add_numbers(1)
add_numbers(2,1,2,1,10)