n,k=input().split(' ')
n,k=[int(n),int(k)]

numbers_consider=[]

for i in range(0,k):
    numbers_consider.append(i+1)


for i in range(1,n+1):
    var=''
    this_set = []

    for j in range(1,i):
        prod=i*j
        not_do=0
        str_prod=str(prod)
        for x in str_prod:
            if int(x) not in numbers_consider or x in this_set:
                not_do=1
            else:
                this_set.append(x)


        if(not_do)==0:
            var+=str(prod)
            if len(this_set)==len(numbers_consider):
                print('{}'.format(i))
        else:
            var=''
            this_set.clear()
            break
