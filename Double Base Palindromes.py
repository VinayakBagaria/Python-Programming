def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

def gen_palin_odd(n):
    x=str(n)
    adder=x[:len(x)-1]
    adder=adder[::-1]
    n=int(x+adder)
    return n

def gen_palin_even(n):
    n=int(str(n)+(str(n)[::-1]))
    return n


limit,base=input().split(' ')
limit,base=[int(limit),int(base)]
numbers=set()

for i in range(1,limit+1):
    numbers.add(gen_palin_even(i))
    numbers.add(gen_palin_odd(i))

numbers=[i for i in numbers if i<limit]
sum_palin=0
for n in numbers:
    x=base10toN(n,base)
    if (x==x[::-1]):
        sum_palin+=n

print(sum_palin)