import random
comGuess=random.randint(0,100)
while 1:
    userInput=int(input('Enter number b/w 0: 100'))
    if userInput>comGuess:
        print('Guess Lower')
    elif userInput<comGuess:
        print('Guess Higher')
    else:
        print('Correct guess')
        break