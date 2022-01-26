import numbers
from random import randint

playerscore = int(300)

play = input ("Do you want to play High-Low Game? Y or N?")
while play.lower()=="y":
    number = randint (1,10)
    guess = input("Guess H for High, L for Low.")
    if guess.lower()=="h":
        if number > 5:
            print("Congratulations, You nailed your guess! The number was", number)
            playerscore = playerscore + 100
            print("Your current score is", playerscore , " points")
            play = input("Do you want to play again? Y or N?")
            if playerscore < 25 :
                print ("Sorry you ran out of points!")
                print ("Don't worry, we've recharge your points")
                playerscore = int(300)

        if number < 6:
            print("You've guessed wrong! The number was ", number)
            playerscore = playerscore - 75
            print("Your current score is", playerscore , " points")
            if playerscore < 25 :
                print ("Sorry you ran out of points!")
                print ("Don't worry, we've recharge your points")
                playerscore = int(300)

    if guess.lower()=="l":
        if number < 6:
            print("Congratulations, You nailed your guess! The number was", number)
            playerscore = playerscore + 100
            print("Your current score is", playerscore , " points")
            play = input("Do you want to play again? Y or N?")
            if playerscore < 25 :
                print ("Sorry you ran out of points!")
                print ("Don't worry, we've recharge your points")
                playerscore = int(300)
        if number > 5:
            print("You've guessed wrong! The number was ", number)
            playerscore = playerscore - 75
            print("Your current score is", playerscore , " points")
            if playerscore < 25 :
                print ("Sorry you ran out of points!")
                print ("Don't worry, we've recharge your points")
                playerscore = int(300)