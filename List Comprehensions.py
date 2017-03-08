# Let's learn about list comprehensions! You are given three integers X,Y,Z and representing the dimensions of a cuboid.
# You have to print a list of all possible coordinates on a 3D grid where the sum of X(i)+Y(i)+Z(i) is not equal to N.
# If X=2, the possible values of can be 0,1 and 2. The same applies to Y and Z.
# I/P : X,Y,Z,N                           O/P : Lexicographical order
xr=int(input())
yr=int(input())
zr=int(input())
n=int(input())
list=[[x,y,z] for x in range(xr+1) for y in range(yr+1) for z in range(zr+1) if(x+y+z!=n)]
print(list)