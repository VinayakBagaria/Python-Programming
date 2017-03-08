import operator

operator_functions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}
 
postfix_expression = "34-5+"
 
stack = []
 
for char in postfix_expression :
    if char in operator_functions:
        no1 = int(stack.pop())
        no2 = int(stack.pop())
        stack.append(operator_functions[char](no2, no1))
    else :
        stack.append(char)
 
print stack.pop()