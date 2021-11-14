from random import randint
from gameComponents import winLose, gameVars, playerComparison

print("***** Welcome to the RPS Stadium *****")

# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    gameVars.player = input("Rock, Paper, Scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("Player chose: " + gameVars.player)
    print("Opponent chose: " + gameVars.computer)

    playerComparison.winner()

    print("Player lives: " + str(gameVars.playerLives))
    print("Opponent lives: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("Lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("Won")

    gameVars.player = False
