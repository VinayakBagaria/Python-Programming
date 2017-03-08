n=int(input())
biggest=0
for i in range(0,n):
    for j in range(0,n):
        power=i**j
        ans=0
        digits = [int(char) for char in str(power)]
        for d in digits:
            ans+=d
        if(ans>biggest):
            biggest=ans
print(biggest)