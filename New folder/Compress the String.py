from itertools import groupby

seq=input()

keyfunc=lambda x:x

for key,group in groupby(seq,key=keyfunc):
    print('({}, {}) '.format(len(list(group)),key),end='')