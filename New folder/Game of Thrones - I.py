"""
We can check if a string will transform into a palindrome if --
    1) Frequency of all the letters is even
    2) Not more than 1 letter may have frequency as odd

Only when these 2 conditions satisfy will the string have an "anagram" which is a  palindrome.
"""

import collections
string=input()
letters=collections.Counter(string)

odd=0

for key in letters:
    if(letters[key]%2!=0):
        odd+=1

if odd>1:
    print('NO')
else:
    print('YES')