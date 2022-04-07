from random import randint
import time
roundCounter, playerScore, opponentScore= 0, 0, 0
print("*" * 23, "Rock Paper Scissors", "*" * 23)
for i in range(5):
    roundCounter = roundCounter + 1
    print("")
    print("=" * 25)
    print("")
    print("ROUND", roundCounter)
    print("")
    print("="*25)
    if i > 0:
        print("CURRENT SCORE:", " " * 8, "|")
        print(" " * 23, "|")
        print("Player:", playerScore, " " * 13, "|")
        print("Computer:", opponentScore, " " * 11, "|")
        print("="*25)
    validInput = False
    while validInput != True:
        print("")
        print("Make your choice!")
        playerInput = input("Rock, Paper or Scissors? (input R, P or S): ").upper()
        if playerInput != "R" and playerInput != "P" and playerInput != "S":
            print("Sorry, but that input is invalid. Enter 'R', 'P' or 'S' to make your choice:")
            print("")
        else:
            if playerInput == "R":
                playerChoice = 0
            elif playerInput == "P":
                playerChoice = 1
            elif playerInput == "S":
                playerChoice = 2
            validInput = True
    opponentChoice = randint (0, 2)
    print("")
    if playerChoice == 0:
        print("You chose Rock...")
    elif playerChoice == 1:
        print("You chose Paper...")
    elif playerChoice == 2:
        print("You chose Scissors...")
    time.sleep(1)
    if opponentChoice == 0:
        print("...and your opponent chose Rock!")
    elif opponentChoice == 1:
        print("...and your opponent chose Paper!")
    elif opponentChoice == 2:
        print("...and your opponent chose Scissors!")
    time.sleep(1)
    print("")
    if opponentChoice == playerChoice:
        print("Draw!")
    elif (playerChoice == 0 and opponentChoice == 2) or (playerChoice == 1 and opponentChoice == 0) or (playerChoice == 2 and opponentChoice == 1):
        print("You win!")
        playerScore = playerScore + 1
    else:
        print("You lose!")
        opponentScore= opponentScore+ 1
    time.sleep(1)
    print("")
print ("")
print ("*" * 23, "GAME OVER", "*" * 23)
print ("")
print("The scores are:")
print ("")
print("Player:", playerScore)
print("Computer:", opponentScore)
print ("")
if playerScore == opponentScore:
    print("It's a draw!")
elif playerScore > opponentScore:
    print("You win!")
else:
    print("You lose!")



