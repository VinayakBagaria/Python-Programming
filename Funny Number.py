test=int(input())
inp=rev=[None]*test

def check():
    flag=-1
    for i in range(test):
        str1=inp[i]
        str2=''.join(reversed(str1))
        print(len(str1))
        for j in range(1,len(str1)):
            print(str1[j],'   ',str2[j])
            diff1=abs((int(str1[j]-str1[j-1])))
            diff2=abs((str1[j]-str2[j-1]))
            if diff1!=diff2:
                flag=0
                break
        if flag==-1:
            print("Funny")
        else:
            print("Not Funny")

for i in range(test):
    inp[i]=input()
check()


