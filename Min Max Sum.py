input_set=sorted([int(x) for x in input().split(' ')])
max=sum(input_set[x] for x in range(1,len(input_set)))
min=sum(input_set[x] for x in range(0,len(input_set)-1))
print('{} {}'.format(min,max))