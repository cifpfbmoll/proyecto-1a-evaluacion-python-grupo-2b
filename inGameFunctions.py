from cardCreationAndDistribution import randomCardDistribution, players
import random

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining, playersPunctuation = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista per agafar, llista de puntuacions

listReversed = False

#Sabem que la forma més optima es no emprar globals però no varem aconseguir fer-ho d'una altra forma
#variables globales: inRound, startingPlayer, currentPlayer, cartaIndex, cartaElegida, robado, listReversed, selectedColor
#+ les de adalat

def mostrarMano():
    global cartaIndex, cartaElegida, robado
    i=1
    for carta in playersCurrentCards[currentPlayer]:
        print("%d)" %(i), end="")
        for atr in carta:
            print(atr, end=" ")
        print()
        i+=1
    print("%d)" %(i), end="")
    print("Robar Carta")
    if (len(alreadyUsedCards) == 1) and (alreadyUsedCards[0][0] == "special"):
        cardIsWild()
    indice = input("Elige un número de tu mano:")
    if (int(indice) == i):
        drawCards()
        cartaElegida = playersCurrentCards[currentPlayer][-1]
        cartaIndex = len(playersCurrentCards[currentPlayer])-1
        robado = True
    else:
        cartaIndex = int(indice)-1
        cartaElegida = playersCurrentCards[currentPlayer][cartaIndex]

def compararCarta():
    #comprovar si la carta que ha robat es pot tirar
    if (robado) and ((cartaElegida[0] != alreadyUsedCards[-1][0]) and (cartaElegida[1] != alreadyUsedCards[-1][1])):
        print("Como no se puede tirar, se pasa al siguiente turno")
        nextPlayerSelect()
    #si sa carta que tira es especial, tirar-la fora comparar
    elif(cartaElegida[0] == "special"):
        tirarCarta()
    #comparador en cas de que canviin es color amb una wild
    elif (alreadyUsedCards[-1][0] == "special") and (cartaElegida[0] == selectedColor):
            tirarCarta()
    #comparador en cas de que sigui carta normal
    elif ((cartaElegida[0] == alreadyUsedCards[-1][0]) or (cartaElegida[1] == alreadyUsedCards[-1][1])):
        tirarCarta()
    else: 
        print("No has elegido una carta correcta")
        mostrarMano()

#def cartaEspecial():
    #comparar si la carta no es un número y ejecutar según el tipo que sea
    #if (type()):

def tirarCarta():
    tirada = playersCurrentCards[currentPlayer].pop(cartaIndex)
    alreadyUsedCards.append(tirada)

def retornarDescartes():
    cardsRemaining = alreadyUsedCards[:]
    del alreadyUsedCards[0,len(alreadyUsedCards)-1]

def cardIsWild():
    global selectedColor
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

def skipCard():
    nextPlayerSelect()

def nextPlayerSelect():
    global currentPlayer
    if currentPlayer == playerList[-1]:
        currentPlayer = 0

    else:
        currentPlayer = currentPlayer + 1
    
    return currentPlayer


def reversalCard():
    global playerList, listReversed
    playerList = list(reversed(playerList))
    if listReversed:
        listReversed = False
    else:
        listReversed = True

def drawCardsAmount():
    if cartaElegida[1] == "draw 2":
        for times in range(0,2):
            drawCards()

    if cartaElegida[1] == "wild draw 4":
        for times in range(0,4):
            drawCards()

def drawCards():
    rnd = round(random.uniform(-0.49, len(cardsRemaining) - 0.5))
    cardToAdd = cardsRemaining.pop(rnd)
    playersCurrentCards[currentPlayer].append(cardToAdd)

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

def playerTurn():
    global currentPlayer, inRound, robado
    robado = False
    startRound()
    print(alreadyUsedCards)
    mostrarMano()
    print("Has elegido: ", end="")
    print(cartaElegida)
    compararCarta()
    if (len(playersCurrentCards[currentPlayer]) == 0):
        finishRound()
        inRound = False
        if (playersPunctuation[currentPlayer] < 500):
            jugar()
    if (len(playersCurrentCards[currentPlayer]) == 1):
        print("UNO")
    currentPlayer = nextPlayerSelect()

def startRound():
    if listReversed:
        reversalCard()
    inRound, startingPlayer, currentPlayer= gameStart(len(playerList)-1,playerList)
    robado = False
    while (inRound):
        playerTurn()#Funció de què passa durant el turn del jugador.
    print ("Has ganado la ronda")
    finishRound()

def gameStart(maxPlayer, playerList):
    startedGame = True
    startingPlayer = round(random.uniform(0.5, maxPlayer+0.49)) #Quin jugador comença (número, no index a la llista)
    currentPlayer = playerList.index(startingPlayer) #Índex del jugador que comença

    return startingPlayer, currentPlayer, startedGame


startRound()