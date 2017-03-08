string=input()
letters=int(input())

count_a=string.count('a')
repeat=letters//len(string)
counter=count_a*repeat


many=letters-repeat*len(string)
more=string[0:many].count('a')
print(counter+more)


