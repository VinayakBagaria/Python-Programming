negatives = []
positives = []
array=[1,2,-4,5,-3,-10]
for elem in array:
  if elem >= 0:
    positives.append(elem)
  else:
    negatives.append(elem)

result = negatives+positives
print(result)