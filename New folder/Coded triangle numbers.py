from math import sqrt

test=int(input())

for i in range(test):
    t=int(input())

    discrim=1+8*t

    if discrim<=0:
        print(-1)
    else:
        solution1=(-1+sqrt(discrim))/2
        solution2=(-1-sqrt(discrim))/2

        if int(solution1)==solution1:
            print(int(solution1))

        elif int(solution2)==solution2:
            print(int(solution2))

        else:
            print(-1)
