from cardCreationAndDistribution import randomCardDistribution, initiateCards, players
import random

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista per agafar

def gameStart(maxPlayer, playerList):
    ongoingRound = True
    while ongoingRound:
        for cardAmount in playersCurrentCards: #Quantitat de cartes de cada jugador.
            if len(cardAmount) == 0: #Si algú en té 0, final de partida.
                ongoingRound = False

        startingPlayer = round(random.uniform(1, maxPlayer)) #Quin jugador comença (número, no index a la llista)
        currentPlayer = playerList.index(startingPlayer)-1 #Índex del jugador que comença
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

cartaElegida = mostrarMano()

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

def tirarCarta():
    

#def playerTurn(player):


#pruebas
#si = mostrarMano()
#print(si)
#compararCarta(si)

def cardIsWild():
    print("Qué color quieres poner?")
    selectedColor = input()
    return selectedColor

colorglobal = cardIsWild()

def drawCards(cartaElegida):
    if cartaElegida[1] == "draw 2":
        for times in range(0,2):
            rnd = round(random.uniform(0,len(cardsRemaining)-1))
            cardsRemaining.pop(rnd)


    if cartaElegida[1] == "wild draw 4":
        for times in range(0,4):
            rnd = round(random.uniform(0,len(cardsRemaining)-1))
            cardsRemaining.pop(rnd)



#def compararCarta():
    #while (selectedcard-color != descartes[-1]) and (selectedcard-num != descartes[-1])

        #print ("Elige otra carta, esta no se puede tirar")
        #llamamos otra vez a la funcion de seleccionar carta

    #if ha intentado tirar todas las cartas y no puede jugar a forzar a robar carta
