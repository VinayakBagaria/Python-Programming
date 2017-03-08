#Takes a complex number and returns the r , angle
from cmath import polar
pol=polar(complex(input()))
# 2 decimal places round off
print("%.2f" % pol[0])
print("%.2f" % pol[1])