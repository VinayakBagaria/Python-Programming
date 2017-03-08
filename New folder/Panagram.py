str=input()
flag=-1
str=str.lower()
for ch in range(ord('a'),ord('z')):
    if(str.count(chr(ch))==0):
        flag=0
        break
if flag==0:
    print("not pangram")
else:
    print("pangram")