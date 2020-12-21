from Test import giveCardsToPlayers, playerSetup, askForPlayers, cardsToPlayers, playerAmount
import random
import math

def inGame(currentPlayer, Players, maxScore):
    while maxScore < 500:
        startRound(currentPlayer, firstRound)
        #PlayerTurn
            # if ThrowCard
                #CompareCard
                    #ActionCard
            # else DrawCard
                #ThrowCard
                    #CompareCard
                        #ActionCard
        #SelectNextPlayer
        finishRound(currentPlayer, Players)
        maxScore = checkMaxScore(Players)
    else:
        endGame()

def startGame():
    Players = giveCardsToPlayers(playerSetup(playerAmount))
    rnd = math.floor(random.uniform(0, len(Players)))
    initialPlayer = Players[rnd] #Index of starting player
    firstRound = True

    return initialPlayer, firstRound, Players

def startRound(initialPlayer, firstRound, Players):
    if firstRound:
        currentPlayer = startGame()[0]
        firstRound = False

    else:
        Players = giveCardsToPlayers(Players)
        currentPlayer = nextPlayer(initialPlayer, Players)
        firstRound = False

    return currentPlayer, firstRound, Players

def finishRound(currentPlayer, Players):
    roundValue = 0
    for player in Players:
        for card in player.cards:
            selectedCard = card
            if selectedCard.n in range(0, 10):
                roundValue += selectedCard.n

            else:
                if selectedCard.c == "Special":
                    roundValue += 50 #Special cards score 50 each

                else:
                    roundValue += 20 #Non Special action cards score 20 each

    Players[currentPlayer].score += roundValue

def endGame(currentPlayer):
    print("Enhorabuena! El jugador", Players[currentPlayer].pos, "ha ganado la partida!")

def checkMaxScore(Players):
    scores = []
    for player in Players:
        scores.append(player.score)
    maxScore = max(scores)

    return maxScore

def nextPlayer(playingPlayer, playerList):
    if playingPlayer == playerList[-1]:
        upcomingPlayer = playerList[0]

    else:
        upcomingPlayer = playerList[playingPlayer + 1]

    return upcomingPlayer


initialPlayer, firstRound, Players = startGame()
currentPlayer, firstRound, Players = startRound(initialPlayer, firstRound, Players)
inGame(currentPlayer, Players, 0)
