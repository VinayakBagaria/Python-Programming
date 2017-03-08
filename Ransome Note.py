from collections import Counter

n1,n2=input().strip().split(' ')
n1,n2=[int(n1),int(n2)]

inp1=[x for x in input().split(' ')]
inp2=[x for x in input().split(' ')]

def ransom_note(magazine, rasom):
    ransom = Counter(rasom)
    mag_words = Counter(magazine)
    for i in rasom:
        if mag_words[i] < ransom[i]:
            return False
    return True

if ransom_note(inp1,inp2):
    print('Yes')
else:
    print('No')

"""
15 17
o l x imjaw bee khmla v o v o imjaw l khmla imjaw x
imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o
"""