from collections import Counter

inp1=input()
inp2=input()

count1=Counter(inp1)
count2=Counter(inp2)

print(count1)
count1.subtract(count2)

print(sum(abs(val) for val in count1.values()))