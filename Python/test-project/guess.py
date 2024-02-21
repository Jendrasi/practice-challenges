from random import randrange

secretNumber = randrange(10)
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    if int(input("Guess:  ")) == secretNumber:
        print("Good guess!")
        break
    guessCount = guessCount + 1
else:
    print("Sorry, try again!")