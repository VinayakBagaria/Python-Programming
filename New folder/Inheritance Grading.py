naming=[x for x in input().split(' ')]
test=input()
arr=[int(x) for x in input().split(' ')]

print('Name: {}, {}'.format(naming[1],naming[0]))
print('ID: {}'.format(naming[2]))

x=sum(arr)/len(arr)
grade=''

if(x>=90 and x<=100):
    grade='O'
elif(x>=80 and x<=90):
    grade='E'
elif (x >= 70 and x <= 80):
    grade = 'A'
elif(x>=55 and x<=70):
    grade='P'
elif(x>=40 and x<=55):
    grade='D'
else:
    grade='T'

print('Grade: {}'.format(grade))