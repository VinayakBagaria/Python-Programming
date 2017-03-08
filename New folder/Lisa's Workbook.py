firs=[int(x) for x in input().strip().split(' ')]
n=firs[0]
m=firs[1]
arr=[int(x) for x in input().split(' ')]        # max problems per chapter
special=0
page=1
for i in range(0,n):
    problemPerChap=arr[i]          # maximum number of problems in a particular chapter
    for j in range(1,problemPerChap+1):   # take each chapter
        if(j==page):
            special+=1
        if(j%m==0 and j!=problemPerChap):   # find last problem in the page by remainder ; if true increment page counter
            page+=1
    page+=1                         # increment page counter if number of problems has finished
print(special)

