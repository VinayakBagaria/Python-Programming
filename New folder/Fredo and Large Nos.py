try:
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    q=int(input())
    while q>0:
        q-=1
        n,m=input().split(' ')
        n=int(n)
        m=int(m)
        check=0
        if(n==0):
            for x in arr:
                if arr.count(x)>=m:
                    print(x)
                    check=1
                    break
            if(check==0):
                print('0')
        else:
            for x in arr:
                if arr.count(x)==m:
                    print(x)
                    check=1
                    break
            if(check==0):
                print('0')
except Exception as ex:
    template = "An exception of type {0} occured. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)