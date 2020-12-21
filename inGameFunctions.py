from cardCreationAndDistribution import randomCardDistribution, players
import random, os

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining, playersPunctuation = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista per agafar, llista de puntuacions

listReversed = False

def limpiarTerminal():
    if os.name=="posix":
        os.system('clear')
    else:
        os.system('cls')

def mostrarMano(currentPlayer):
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

    if ((primeraJugada) and (alreadyUsedCards[-1][0] == "special")):
        cardIsWild()

    indice = input("Elige un número de tu mano:")

    if ((int(indice) >= 1) and (int(indice) <= i)):
        if (int(indice) == i):
            drawCards(currentPlayer)
            cartaElegida = playersCurrentCards[currentPlayer][-1]
            cartaIndex = len(playersCurrentCards[currentPlayer])-1
            robado = True
        else:
            cartaIndex = int(indice)-1
            cartaElegida = playersCurrentCards[currentPlayer][cartaIndex]
    else:
        print("No has puesto un número de una carta")
        mostrarMano(currentPlayer)
        print (len(playersCurrentCards[currentPlayer])+1)

def compararCarta(currentPlayer):
    #comprovar si la carta que ha robat es pot tirar
    if (robado) and ((cartaElegida[0] != alreadyUsedCards[-1][0]) and (cartaElegida[1] != alreadyUsedCards[-1][1])):
        input("Como no se puede tirar, se pasa al siguiente turno")
        nextPlayerSelect(currentPlayer)
    #si sa carta que tira es especial, tirar-la fora comparar i elegir color
    elif(cartaElegida[0] == "special"):
        cardIsWild()
        tirarCarta(currentPlayer)
    #comparador en cas de que canviin es color amb una wild
    elif (alreadyUsedCards[-1][0] == "special") and (cartaElegida[0] == selectedColor):
            tirarCarta(currentPlayer)
    #comparador en cas de que sigui carta normal
    elif ((cartaElegida[0] == alreadyUsedCards[-1][0]) or (cartaElegida[1] == alreadyUsedCards[-1][1])):
        tirarCarta(currentPlayer)
    else:
        limpiarTerminal()
        print("No has elegido una carta correcta, vuelve a probar")
        print("Última carta tirada:",alreadyUsedCards[-1])
        mostrarMano(currentPlayer)
    
    return currentPlayer

def tirarCarta(currentPlayer):
    currentPlayer = esAccion(currentPlayer)
    tirada = playersCurrentCards[currentPlayer].pop(cartaIndex)
    alreadyUsedCards.append(tirada)

    return currentPlayer

def esAccion(currentPlayer):
    if (type(cartaElegida[1]) is str):
        if (cartaElegida[1] == "reverse"):
            reversalCard()
        elif (cartaElegida[1] == "draw 2") or (cartaElegida[1] == "draw 4"):
            currentPlayer = nextPlayerSelect(currentPlayer)
            drawCardsAmount(currentPlayer)
        else:
            currentPlayer = skipCard(currentPlayer)
    
    return currentPlayer

def retornarDescartes():
    cardsRemaining = alreadyUsedCards[:]
    del alreadyUsedCards[0,len(alreadyUsedCards)-1]

def cardIsWild():
    global selectedColor
    print("Qué color quieres poner? \n 1) Red \n 2) Blue \n 3) Green \n 4) Yellow")
    choice = int(input())
    if ((int(choice) >= 1) and (int(choice) <= 4)):
        if choice == 1:
            selectedColor = "red"

        elif choice == 2:
            selectedColor = "blue"

        elif choice == 3:
            selectedColor = "green"

        elif choice == 4:
            selectedColor = "yellow"
    else:
        print("No has puesto un color disponible")
        cardIsWild()

def skipCard(currentPlayer):
    currentPlayer = nextPlayerSelect(currentPlayer)

    return currentPlayer

def nextPlayerSelect(currentPlayer):
    if currentPlayer+1 == len(playerList):
        currentPlayer = 0
    else:
        currentPlayer += 1
    return currentPlayer

def reversalCard():
    global playerList, listReversed
    playerList = list(reversed(playerList))
    if listReversed:
        listReversed = False
    else:
        listReversed = True

def drawCardsAmount(currentPlayer):
    if cartaElegida[1] == "draw 2":
        for times in range(0,2):
            drawCards(currentPlayer)

    if cartaElegida[1] == "wild draw 4":
        for times in range(0,4):
            drawCards(currentPlayer)

def drawCards(currentPlayer):
    rnd = round(random.uniform(-0.49, len(cardsRemaining) - 0.5))
    cardToAdd = cardsRemaining.pop(rnd)
    playersCurrentCards[currentPlayer].append(cardToAdd)

def finishRound(currentPlayer):
    roundValue = 0
    for playerCards in playersCurrentCards:
        cardsToSum = True
        while cardsToSum:
            if len(playerCards) == 0:
                cardsToSum = False

            cardRemoved = playerCards.pop(0)

            if cardRemoved[0] != "special" and cardRemoved[1] != "skip" and cardRemoved[1] != "reverse" \
            and cardRemoved[1] != "draw 2":
                roundValue = roundValue + cardRemoved[1]

            elif cardRemoved[0] == "special":
                roundValue = roundValue + 50

            elif cardRemoved[1] == "skip" or cardRemoved[1] == "reversed" or cardRemoved[1] == "draw 2":
                roundValue = roundValue + 20


        playersPunctuation[currentPlayer].append(roundValue)

def startRound():
    global inRound, startingPlayer, robado
    inRound = True
    robado = False
    #if listReversed:
        #reversalCard()

def playerTurn(currentPlayer):
    global inRound, robado
    robado = False
    
    startRound()
    limpiarTerminal()
    print("Turno del jugador:",playerList[currentPlayer])
    input("Apreta Intro para iniciar el turno")
    print("Última carta tirada:",alreadyUsedCards[-1])
    if ('selectedColor' in globals() and alreadyUsedCards[-1][0] == "special"):
        print("Color elegido:",selectedColor)
    mostrarMano(currentPlayer)
    print("Has elegido: ", end="")
    print(cartaElegida)
    currentPlayer = compararCarta(currentPlayer)
    if (len(playersCurrentCards[currentPlayer]) == 0):
        finishRound()
        inRound = False
        if (playersPunctuation[currentPlayer] <= 500):
            startRound()
        else:
            print("Enhorabuena! El jugador", playerList[currentPlayer], "ha ganador la partida")
    if (len(playersCurrentCards[currentPlayer]) == 1):
        print("UNO")


def gameStart(maxPlayer, playerList):
    global inRound, startingPlayer, primeraJugada
    primeraJugada = True
    inRound = True
    startingPlayer = round(random.uniform(0.5, maxPlayer+0.49)) #Quin jugador comença (número, no index a la llista)
    currentPlayer = playerList.index(startingPlayer) #Índex del jugador que comença

    return currentPlayer

def jugar():
    global primeraJugada
    currentPlayer = gameStart(len(playerList), playerList)
    while (inRound):
        playerTurn(currentPlayer)#Funció de què passa durant el turn del jugador.
        currentPlayer = nextPlayerSelect(currentPlayer)
        if (cartaElegida[1] == "skip"):
            currentPlayer = nextPlayerSelect(currentPlayer)
        primeraJugada = False
    print("Has ganado la ronda")
    finishRound()

    return currentPlayer


currentPlayer = jugar()
