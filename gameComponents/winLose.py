from gameComponents import gameVars


def winorlose(status):
    print("You " + status)

    choice = input("Would you like to play another round? y/n: ")

    if choice == "n":
        print("***** Catch ya Later! *****")
        exit()
    elif choice == "y":
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
