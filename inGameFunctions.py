from cardCreationAndDistribution import randomCardDistribution, players
import random

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining, playersPunctuation = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista per agafar, llista de puntuacions

listReversed = False

def gameStart(maxPlayer, playerList):
    startingPlayer = round(random.uniform(0.5, maxPlayer+0.49)) #Quin jugador comença (número, no index a la llista)
    currentPlayer = playerList.index(startingPlayer) #Índex del jugador que comença
    playerTurn(currentPlayer) #Funció de què passa durant el turn del jugador.

    return currentPlayer, startingPlayer

currentPlayer = gameStart(len(playerList),playerList)

def playerTurn(currentPlayer):
    #pruebas
    si = mostrarMano(currentPlayer)
    print(si)
    #compararCarta()
    tirarcarta()
    print (alreadyUsedCards)
    print (alreadyUsedCards)

def mostrarMano(currentPlayer):
    i=1
    for carta in playersCurrentCards[currentPlayer]:
        print("%d)" %(i), end="")
        for atr in carta:
            print(atr, end=" ")
        print()
        i+=1
    indice = input("Elige un número de tu mano:")

    cartaElegida = playersCurrentCards[currentPlayer][int(indice)-1]
    return cartaElegida

cartaElegida = mostrarMano(currentPlayer)

def compararCarta():
    #comparador en cas de que canviin es color amb una wild
    if (alreadyUsedCards[-1][0] == "special"):
        if (cartaElegida[0] == colorglobal):
            #tirarcarta
            print("carta especial")
    #comparador en cas de que sigui carta normal
    elif ((cartaElegida[0]=="a") or (cartaElegida[1]=="b")):
        #tirarcarta
        print("carta normal")

def tirarcarta():
    tirada = playersCurrentCards[currentPlayer[cartaTirada]].pop
    alreadyUsedCards.insert(-1, tirada)

def cardIsWild():
    print("Qué color quieres poner? \n 1) Red \n 2) Blue \n 3) Green \n 4) Yellow")
    choice = int(input())
    if choice == 1:
        selectedColor = "red"

    elif choice == 2:
        selectedColor = "blue"

    elif choice == 3:
        selectedColor = "green"

    elif choice == 4:
        selectedColor = "yellow"

    return selectedColor

def skipCard():
    nextPlayerSelect(nextPlayerSelect(currentPlayer))

def nextPlayerSelect(currentPlayer):
    if currentPlayer == playerList[-1]:
        nextPlayer = playerList[0]

    else:
        nextPlayer = currentPlayer + 1

    return nextPlayer

def reversalCard(playerList, listReversed):
    playerList = list(reversed(playerList))
    if listReversed:
        listReversed = False
    else:
        listReversed = True

    return playerList, listReversed

def drawCardsAmount(cartaElegida):
    if cartaElegida[1] == "draw 2":
        for times in range(0,2):
            drawCards()

    if cartaElegida[1] == "wild draw 4":
        for times in range(0,4):
            drawCards()

def drawCards(nextPlayer):
    rnd = round(random.uniform(-0.49, len(cardsRemaining) - 0.5))
    cardToAdd = cardsRemaining.pop(rnd)
    cardToAdd.append(playersCurrentCards[nextPlayer])

def finishRound():
    roundValue = 0
    for player in playersCurrentCards:
        cardsToSum = True
        while cardsToSum:
            cardRemoved = playersCurrentCards[player].pop(0)

            if cardRemoved[0] != "special" and cardRemoved[1] != "skip" and cardRemoved[1] != "reverse" \
            and cardRemoved[1] != "draw 2":
                roundValue = roundValue + cardRemoved[1]

            elif cardRemoved[0] == "special":
                roundValue = roundValue + 50

            elif cardRemoved[1] == "skip" or cardRemoved[1] == "reversed" or cardRemoved[1] == "draw 2":
                roundValue = roundValue + 20

            if len(playersCurrentCards[player]) == 0:
                cardsToSum = False

        playersPunctuation[currentPlayer].append(roundValue)

def startRound(startingPlayer):
    if listReversed:
        reversalCard()

    startingPlayer = nextPlayerSelect(startingPlayer)
    currentPlayer = playerList.index(startingPlayer)

    return currentPlayer, startingPlayer