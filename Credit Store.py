'''
Problem
You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all
available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide
will consist of the two integers indicating the positions of the items in your list (smaller number first).

Input
The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:
    One line containing the value C, the amount of credit you have at the store.
    One line containing the value I, the number of items in the store.
    One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
    Each test case will have exactly one solution.

Output
For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store
credit. The lower index should be output first.
'''
test=int(input())
have=test
result1=[None]*test
result2=[None]*test
count=0
while(test>0):
    c=int(input())  #get credit value

    l=int(input())   #get prices
    line=input()
    x=line.split(' ')

    dict1={}      #store the prices in a dictionary
    for i in range(0,l):
        dict1[i+1]=x[i]

    for i in range(0,l):
        done=-1

        value=c-int(x[i])    #get the expeted output
        v=str(value)

        for j in range(i+2,l+1):   #get the key value of the difference if it exists
            if(dict1[j]==v):
                result1[count]=i+1
                result2[count]=j
                count=count+1
                done=0
                break
        if(done==0):
            break
    test=test-1

for i in range(0,have):
    print('Case #{0}: {1} {2}'.format(i+1,result1[i],result2[i]))