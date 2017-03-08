def get_res():
    max_a=max(ele_a)
    min_b=min(ele_b)

    count=0

    for i in range(max_a,min_b+1):
        if (sum(1 for x in ele_a if i % x == 0) == len(ele_a)):
            if (sum(1 for x in ele_b if x % i == 0) == len(ele_b)):
                count += 1

    return count

num_a,num_b=input().strip().split(' ')
num_a,num_b=[int(num_a),int(num_b)]

ele_a=[int(x) for x in input().strip().split(' ')]
ele_b=[int(x) for x in input().strip().split(' ')]

print(get_res())