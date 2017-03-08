n=int(input())
string=input()
k=int(input())%26

new=''

for i in range(0,n):
    c=ord(string[i])


    if(c>=97 and c<=122):

        val = c+k
        if(val>122):
            val= val - 122 + 97 - 1
        c = val
    elif(c>=65 and c<=90):
        val = c + k
        if (val > 90):
            val = val - 90 + 65 - 1
        c = val

    new+=chr(c)
print(new)