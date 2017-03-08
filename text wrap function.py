import textwrap
st=input()
'''
    textwrap.wrap(string,int) - makes a list of elemenets with at most 'int' chars only
    print(textwrap.wrap(st,int(input())))
'''
# textwrap.fill(string,int) - displays the elements with at most 'n' chars in different lines
print(textwrap.fill(st,int(input())))