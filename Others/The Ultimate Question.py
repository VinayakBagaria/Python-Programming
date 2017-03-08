line=input()
x=line.split(' ')
a=int(x[0])
b=int(x[1])
c=int(x[2])
if a+b+c==42:
    print('{0}+{1}+{2}'.format(a,b,c))
elif a+(b*c)==42:
    print('{0}+{1}*{2}'.format(a,b,c))
elif a*b+c==42:
    print('{0}*{1}+{2}'.format(a,b,c))
elif a*b*c!=42:
    print('{0}*{1}*{2}'.format(a,b,c))
else:
    print('This is not the ultimate question.')