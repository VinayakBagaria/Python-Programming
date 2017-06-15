string=[x for x in input().split(' ')]

landmark_count=int(input())
landmarks=[x for x in input().split(' ')]
output=''
for word in string:
    if word in landmarks:
        output+='<b>'+word+'</b>'
    else:
        output+=word
    output+=' '
print(output)