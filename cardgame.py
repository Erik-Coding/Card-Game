import time
import math
import random

# TO-DO
# MAKE NEW FUNCTIONS ON P2 SIDE
# re-do code into functions


deck = [3,4,5,6,7,8,9,10,11,12,13,14]

playerOneTurn = True

playerOneTotal = 0
playerTwoTotal = 0

playerOneWins = 0
playerTwoWins = 0

playerOneOver = False
playerTwoOver = False

playerOnePerfectScore = False
playerTwoPerfectScore = False

def drawCard(player):
    global playerOneTotal
    global playerTwoTotal
    global deck

    if (player == 1):

        drewCardRisk = deck[0]
        deck.remove(deck[0])
        deck.append(drewCardRisk)

        return drewCardRisk

    elif (player == 2):

        drewCardRisk2 = deck[0]
        deck.remove(deck[0])
        deck.append(drewCardRisk2)

        return drewCardRisk2
        
def riskFunctionAsk():
    while True:
        riskAsk = input("\nDo you want to risk or keep? (Risk/Keep) ")
        if (riskAsk.lower()[0] == "r"):
            return True
            break

        elif (riskAsk.lower()[0] == "k"):
            return False
            break
        else: 
            print("Please input a \"Risk\" or a \"Keep\".")

def playAgain():
    while True:
        plrInput = input("Would you like to play again? ")

        if (plrInput.lower()[0] == "y"):
            return True
            break
        
        elif (plrInput.lower()[0] == "n"):
            return False
            break
        
        else:
            print("Please Input a Yes or a No.")



def setVars():
    global playerOneOver
    global playerTwoOver
    global playerOnePerfectScore
    global playerTwoPerfectScore
    global playerOneTotal
    global playerTwoTotal

    playerOneOver = False
    playerTwoOver = False

    playerOnePerfectScore = False
    playerTwoPerfectScore = False

    playerOneTotal = 0
    playerTwoTotal = 0 

def shuffle():
    global deck

    print("Shuffling the cards...")
    time.sleep(2)
    random.shuffle(deck)

def printRound(rounds):
    print("\nRound", rounds + 1)
    time.sleep(2)

def drawFirstCard():
    global deck

    # draw first card
    drewCardStart = deck[0]
    deck.remove(deck[0])
    deck.append(drewCardStart)

    return drewCardStart

def checkPlayerTotal(plr):
    global playerOneOver
    global playerOnePerfectScore

    global playerTwoOver
    global playerTwoPerfectScore

    if (plr == 1):

        if (playerOneTotal > 26):
            print("\nYou got more than 26, you lose! For now... If Player 2 get's over 26, this round won't count!")
            playerOneOver = True

            return "Over"
        elif (playerOneTotal == 26):
            print("\nYou got 26! Let's see what Player 2 can do...")
            playerOnePerfectScore = True

            return "Perfect"

    elif (plr == 2):

        if (playerTwoTotal > 26):
            print("\nYou got more than 26, you lose! For now... If Player 2 get's over 26, this round won't count!")
            playerTwoOver = True

            return "Over"
        elif (playerTwoTotal == 26):
            print("\nYou got 26! Let's see what Player 2 can do...")
            playerTwoPerfectScore = True

            return "Perfect"

def checkWhoWon(oneTotal, twoTotal):

    global playerOneOver
    global playerTwoOver
    global playerOneWins
    global playerTwoWins

    if (playerOneOver and playerTwoOver):
        print("You BOTH got over 26! This round won't count ):")
    
    elif (playerOneOver):
        playerTwoWins = playerTwoWins + 1
        print(f"Player one got over 26! Player two wins {playerTwoWins} wins")
    
    elif (playerTwoOver):
        playerOneWins = playerOneWins + 1
        print(f"Player two got over 26! Player one wins {playerOneWins} wins")
    
    elif (playerOneTotal == playerTwoTotal):
        print("It's a tie!!")
    
    elif (playerOneTotal > playerTwoTotal):
        playerOneWins = playerOneWins + 1
        print(f"Player one got closer to 26! Player one wins and has {playerOneWins} wins")
    
    elif (playerOneTotal < playerTwoTotal):
        playerTwoWins = playerTwoWins + 1
        print(f"Player two got closer to 26! Player two wins!!! and has {playerTwoWins} wins")

def whoHasWins(oneWins, twoWins):
    if (oneWins < twoWins):
        print(f"Player two had more wins! Player one wins: {oneWins}. Player two wins: {twoWins}")
    elif (oneWins > twoWins):
        print(f"Player one had more wins! Player one wins: {oneWins}. Player two wins: {twoWins}")

while True:
    

    setVars()

    
    for rounds in range(5):

        setVars()
        shuffle()

        printRound(rounds)

        while playerOneTurn: # P1 Turns

            drewCardStart = drawFirstCard()

            playerOneTotal = drewCardStart

            print("\nPlayer one, you drew a", drewCardStart, "/ 26.")
            time.sleep(1)
            
            while True: # Drawing Section for P1

                # ask P1 if they want to risk or keep
                riskQuestion = riskFunctionAsk()

                if (riskQuestion):
                    print("\nOkay, you risked! We will draw another card!")
                    time.sleep(2)
                    
                    drewCard = drawCard(1)

                    # add drew card to player 1 total
                    playerOneTotal = playerOneTotal + drewCard
                    print("\nYou drew a", str(drewCard) + ". You now have", playerOneTotal, "/ 26.")


                    plrTotalCheck = checkPlayerTotal(1)

                    if (plrTotalCheck == "Over"):
                        break
                    elif (plrTotalCheck == "Perfect"):
                        break

                elif (riskQuestion == False):
                    print("\nOkay, Player 2's turn!")
                    time.sleep(2)
                    break

                else: 
                    print("\nPlease Input a \"Risk\" or a \"Keep\"")
            
            playerOneTurn = False

        while playerOneTurn == False: # P2s turn

            # draw first card                
            drewCardStart2 = drawFirstCard()

            playerTwoTotal = drewCardStart2

            print("\nPlayer Two, you drew a", playerTwoTotal, "/ 26.")
            time.sleep(1)
            
            while True: # Drawing Section for P2

                riskQuestion = riskFunctionAsk()

                if (riskQuestion):
                    print("\nOkay, you risked! We will draw another card!")
                    time.sleep(2)

                    # draw another card
                    drewCard2 = drawCard(2)

                    playerTwoTotal = playerTwoTotal + drewCard2
                    print("\nYou drew a", str(drewCard2) + ". You now have", playerTwoTotal, "/ 26.")

                    plrTotalCheck = checkPlayerTotal(2)

                    if (plrTotalCheck == "Over"):
                        break
                    elif (plrTotalCheck == "Perfect"):
                        break

                elif (riskQuestion == False):
                    print("\nOkay, let's see who won!")
                    time.sleep(2)
                    break

                else: 
                    print("\nPlease Input a \"Risk\" or a \"Keep\"")

            playerOneTurn = True

        # checking who won
        checkWhoWon(playerOneTotal, playerTwoTotal)
             

    playAgainQuestion = playAgain()

    whoHasWins(playerOneWins, playerTwoWins)

    if (playAgainQuestion == True):
        continue
    elif (playAgainQuestion == False):
        break