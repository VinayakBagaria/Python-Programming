test=int(input())
store=[0]*test
for i in range(0,test):
    store[i]=int(input())
for i in range(0,test):
    print(pow(store[i],2,10**9+7))