n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    string=input().strip()

    if string=='pop':
        s.pop()
    elif 'remove' in string:
        s.remove(int(string.split(' ')[1]))
    else:
        s.discard(int(string.split(' ')[1]))

print(sum(s))
