import random

hiddenNumber = random.randint(1,50)

userGuess = 0

while not userGuess == hiddenNumber:

    userGuess = int(input('Guess a number: '))

    if userGuess > hiddenNumber:
        print('Too high')
    elif userGuess < hiddenNumber:
        print('Too low')
    else:
        print("that's right")
