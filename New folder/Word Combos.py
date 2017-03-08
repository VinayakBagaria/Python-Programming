'''
    Both players are given the same string,S .
    Both players have to make substrings using the letters of the string.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.
'''
s=input()
l=len(s)
player1,player2=0,0
for i in range(l):
    if s[i] in 'AEIOU':
        player1+=l-i
    else:
        player2+=l-i
if player1>player2:
    print("Kevin ",player1)
elif player1<player2:
    print("Stuart ",player2)
else:
    print('Draw')