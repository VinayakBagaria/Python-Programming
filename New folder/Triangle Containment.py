#include <stdio.h>
#include <stdlib.h>

def area(x1,y1,x2,y2,x3,y3):
   return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)


def isInside(x1,y1,x2,y2,x3,y3):
    x=0
    y=0
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)

    A1 = area (x, y, x2, y2, x3, y3)

    A2 = area (x1, y1, x, y, x3, y3)

   A3 = area (x1, y1, x2, y2, x, y)

   # Check if sum of A1, A2 and A3 is same as A
   return (A == A1 + A2 + A3);

