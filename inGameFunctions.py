from cardCreationAndDistribution import randomCardDistribution, initiateCards, players
import random

playerList, playersCurrentCards, alreadyUsedCards, cardsRemaining = randomCardDistribution(players)
#Llista amb jugadors, llista amb cartes actuals, llista descartes, llista

def gameStart(maxPlayer, playerList):
    ongoingRound = True
    while ongoingRound:
        for cardAmount in playersCurrentCards: #Quantitat de cartes de cada jugador.
            if len(cardAmount) == 0: #Si algú en té 0, final de partida.
                ongoingRound = False

        startingPlayer = round(random.uniform(1, maxPlayer)) #Quin jugador comença (número, no index a la llista)
        currentPlayer = playerList.index(startingPlayer) #Índex del jugador que comença
        #playerTurn(currentPlayer) #Funció de què passa durant el turn del jugador.

randomCardDistribution()

def compararCarta():
    for carta in cardsRemaining:
        for i in range(len(cardsRemaining)):
            print(i, end="")
        print(carta, end="")
    int(input("Elige un número de tu mano:"))

def compararCarta():
    while (selectedcard-color != descartes[-1]) and (selectedcard-num != descartes[-1])

        print ("Elige otra carta, esta no se puede tirar")
        #llamamos otra vez a la funcion de seleccionar carta

    #if ha intentado tirar todas las cartas y no puede jugar a forzar a robar carta

