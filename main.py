from random import randint
from gameComponents import winLose, gameVars

print("***** Welcome to the RPS Stadium *****")

# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    gameVars.player = input("Rock, Paper, Scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("Player chose: " + gameVars.player)
    print("Opponent chose: " + gameVars.computer)

    if gameVars.computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print("Tie! Try again")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("You Lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You Win!")
            gameVars.computerLives = gameVars.computerLives - 1

    print("Player lives: " + str(gameVars.playerLives))
    print("Opponent lives: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("Lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("Won")

    gameVars.player = False
