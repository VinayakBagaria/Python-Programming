def check(y,x):
    for i in range(0,obstacle):
        if(x==ob_x[i] and y==ob_y[i]):
            return 1
    return 0

sidelength,obstacle=input().split(' ')
sidelength,obstacle=[int(sidelength),int(obstacle)]

"""
(y,x)
4,4  and size 8,8
left : 4,3 4,2 4,1 [decrease x till 1]
right : increase x increase x till 8
up : increase y till 8
down : decrease y till 1
nw : increase y, decrease x till x=1 and y=8
ne : increase y, increase x till x=8 and y=8
sw : decrease y, decrease x till x=1 and y=1
se : decrease y, increase x till x=8 and y=1
"""

y,x=input().split(' ')
y,x=[int(y),int(x)]

ob_x=[]
ob_y=[]

for i in range(0,obstacle):
    a,b=input().split(' ')
    a,b=[int(a),int(b)]
    ob_y.append(a)
    ob_x.append(b)

moves=0


# left
leftX=x
while(leftX!=1):
    if(check(y,leftX-1)==1):
        break
    moves+=1
    leftX-=1


#right
rightX=x
while(rightX!=sidelength):
    if (check(y,rightX+1) == 1):
        break
    moves+=1
    rightX+=1


# up
upY = y
while (upY != sidelength):
    if (check(upY+1,x) == 1):
        break
    moves += 1
    upY += 1

# down
downY = y
while (downY != 1):
    if (check(downY-1,x) == 1):
        break
    moves += 1
    downY -= 1


#nw
incY=y
decX=x
while(decX!=1 and incY!=sidelength):
    if (check(incY+1, decX-1) == 1):
        break
    moves+=1
    decX-=1
    incY+=1

#ne
incY=y
incX=x
while(incX!=sidelength and incY!=sidelength):
    if (check(incY+1, incX+1) == 1):
        break
    moves+=1
    incX+=1
    incY+=1

#sw
decY=y
decX=x
while(decX!=1 and decY!=1):
    if (check(decY-1, decX-1) == 1):
        break
    moves+=1
    decX-=1
    decY-=1


#se
decY=y
incX=x
while(incX!=sidelength and decY!=1):
    if (check(decY-1, incX+1) == 1):
        break
    moves+=1
    incX+=1
    decY-=1

print(moves)