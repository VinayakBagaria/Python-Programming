def makePalin(str,count):
    start=0
    end=len(str)-1
    while(start<end):
        if str[start]!=str[end]:
            count=count+1
            break
            str=str+str[start]
            start=0
            end=len(str)-1
        else:
            start=start+1
            end=end-1


s=input()
count=0
makePalin(s,count)