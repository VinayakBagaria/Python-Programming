start_x,start_y=input().strip().split(' ')
start_x,start_y=[int(start_x),int(start_y)]

sum_x,sum_y=0,0
for i in range(0,int(input())):
    now_x, now_y = input().strip().split(' ')
    now_x, now_y = [int(now_x), int(now_y)]

    sum_x+=now_x
    sum_y+=now_y

print('{} {}'.format(start_x-sum_x,start_y-sum_y))