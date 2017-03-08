import Stack
def evalPostfix(text):
    s = Stack()
    for symbol in text:
        try:
            result = int(symbol)
        except ValueError:
            if symbol not in '+-*/':
                raise ValueError('text must contain only numbers and operators')
            result = eval('%d %s %d' % (s.pop(), symbol, s.pop()))
        s.push(result)
    return s.pop()

print(evalPostfix(5 4 +))