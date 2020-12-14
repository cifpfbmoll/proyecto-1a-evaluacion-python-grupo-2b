from cardCreationAndDistribution import randomCardDistribution, players
import random

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista per agafar

def gameStart(maxPlayer, playerList):
    ongoingRound = True
    while ongoingRound:
        for cardAmount in playersCurrentCards: #Quantitat de cartes de cada jugador.
            if len(cardAmount) == 0: #Si algú en té 0, final de partida.
                ongoingRound = False

    startingPlayer = round(random.uniform(0.5, maxPlayer+0.49)) #Quin jugador comença (número, no index a la llista)
    currentPlayer = playerList.index(startingPlayer) #Índex del jugador que comença
    playerTurn(currentPlayer) #Funció de què passa durant el turn del jugador.
    print(currentPlayer)

    return currentPlayer

currentPlayer = gameStart(len(playerList),playerList)

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
    elif (cartaElegida[0]==) or (cartaElegida[1]):
        #tirarcarta
        print("carta normal")

def playerTurn(currentPlayer):

#pruebas
si = mostrarMano()
print(si)
compararCarta(si)

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

def reversalCard(playerList):
    playerList = list(reversed(playerList))
    return playerList

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
