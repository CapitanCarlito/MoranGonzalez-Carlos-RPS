from random import randint
from gameComponents import winLose, gameVars

def winner():
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