m,n=input().split(' ')
arr = []

for arr_i in range(int(m)):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(arr)