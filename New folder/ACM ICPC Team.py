import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

result = []
for i in range(n-1):
    for j in range(i+1,n):
        result.append(str(bin(int(topic[i],2) | int(topic[j],2))[2:]).count('1'))

print(max(result))
print(result.count(max(result)))