width=[int(n) for n in input().split(' ')]
ascii=[chr(x+97) for x in range(26)]
diction=dict(zip(ascii,width))

input_string=input().lower()

max=0
for x in input_string:
    if(max<diction.get(x)):
        max=diction.get(x)

print(len(input_string)*max)
