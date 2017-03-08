string=input()
stack=[]

stack.append('')

for a in string:
    length=len(stack)
    if(stack[len(stack)-1]==a):
        stack.pop()
    else:
        stack.append(a)

if len(stack)==1:
    print('Empty String')
else:
    result=''.join(x for x in stack)
    print(result)