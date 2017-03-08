def maxXor(l, r):
    ans=0
    for i in range(l,r+1):
        for j in range(l,r+1):
            temp=(i|j)&~(i&j)
            if ans<temp:
                ans=temp
    return ans

if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))