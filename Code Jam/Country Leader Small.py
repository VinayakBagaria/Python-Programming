test=int(input())

for i in range(0,test):
    n=int(input())
    counts=dict()
    for k in range(0,n):
        string=input()
        counts[string]=len(set(''.join(string.split(' '))))

    maxVal=max(counts.values())
    countList=[name for name in counts.keys() if counts[name]==maxVal]
    print('Case #{}: {}'.format(i+1,sorted(countList)[0]))

