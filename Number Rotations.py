sum=0
for i in range(11,10**int(input())):
    number=str(i)
    rotated=number[len(number)-1]+number[:-1]

    if(int(rotated)%i==0):
        sum+=i

print(sum)
