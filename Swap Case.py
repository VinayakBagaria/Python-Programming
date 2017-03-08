str=input()
s=""
for i in str:
    if i.isupper():
        s=s+i.lower()
    else:
        s=s+i.upper()

print(s)