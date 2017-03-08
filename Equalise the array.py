n=input()
list_num=[int(x) for x in input().strip().split(' ')]


print(len(list_num)-max([list_num.count(i) for i in list_num]))