n=int(input())

phi=(1+pow(5,0.5))/2
rev=(1-pow(5,0.5))/2

element=((pow(phi,n)-pow(rev,n))/pow(5,0.5))
print(int(element))