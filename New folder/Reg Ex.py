import re
regex=r"1[0]+1"

for i in range(int(input())):
    pattern=input()
    patternCount=0

    while(1):
        matches=re.search(regex,pattern)
        try:
            pattern=pattern[matches.end()-1:]
            patternCount+=1
        except:
            break
    print(patternCount)

