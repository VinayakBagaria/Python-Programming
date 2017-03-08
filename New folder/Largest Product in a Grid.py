arr=[]

for i in range(20):
    arr_t=[int(x) for x in input().strip().split(' ')]
    arr.append(arr_t)


product=0

for col in range(20):
    for row in range(20):

        # check vertically
        if row<16:
            prod=arr[col][row]*arr[col][row+1]*arr[col][row+2]*arr[col][row+3]

        product=max(product,prod)

        # check horizontally
        if col < 16:
            prod = arr[col][row] * arr[col+1][row] * arr[col+2][row] * arr[col+3][row]

        product = max(product,prod)

        # check one way of diagonal
        if(col<16 and row>=4):
            prod=arr[col][row]*arr[col+1][row-1]*arr[col+2][row-2]*arr[col+3][row-3]

        product = max(product,prod)

        # check other way of diagonal
        if (col < 16 and row < 16):
            prod = arr[col][row] * arr[col + 1][row + 1] * arr[col + 2][row + 2] * arr[col + 3][row + 3]

        product = max(product,prod)

print(product)