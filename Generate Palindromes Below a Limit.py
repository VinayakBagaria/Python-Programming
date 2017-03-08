def gen_palin_odd(n):
    x=str(n)
    adder=x[:len(x)-1]
    adder=adder[::-1]
    n=int(x+adder)
    return n

def gen_palin_even(n):
    n=int(str(n)+(str(n)[::-1]))
    return n


limit=int(input())
numbers=set()

for i in range(1,limit+1):
    numbers.add(gen_palin_even(i))
    numbers.add(gen_palin_odd(i))

numbers=[i for i in numbers if i<limit]
print(numbers)