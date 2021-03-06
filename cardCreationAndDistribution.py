import random


class Card:
    def __init__(self, col, num):
        self.c = col
        self.n = num

def initiateCards():

    doubleCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "reverse", "draw 2", "skip"]
    colors = ["red", "green", "blue", "yellow"]
    specialCards = ["wild", "wild draw 4"]
    cardList = []

    for color in colors:
        for specialCard in specialCards:
            initCards = Card("special", specialCard)
            cardList.append([initCards.c, initCards.n])
        initCards = Card(color, 0)
        cardList.append([initCards.c, initCards.n])
        for card in doubleCards:
            for z in range(0, 2):
                initCards = Card(color, card)
                cardList.append([initCards.c, initCards.n])
    return cardList

def playerSetup():
    print("Cuántos jugadores?")
    playerAmount = int(input())

    return playerAmount

players = playerSetup()

def randomCardDistribution(playerAmount):
    playerAmountList = list(range(1, playerAmount + 1)) #Guarda les posicions dels jugadors.

    if len(playerAmountList) < 1 or len(playerAmountList) > 10:
        print("Error! Número de jugadores inválido! Deben ser más de 1 y como mucho, 10.")

    else:
        cardList = initiateCards()
        playersCards = []
        playersPunctuation = []
        for createList in playerAmountList: #Creació llista per cartes de jugadors.
            playersCards.append([])
            playersPunctuation.append([])

        for cardsToDistribute in range(7): #Distribució de cartes.
            for cardsToPlayer in range(len(playerAmountList)):
                rnd = round(random.uniform(-0.49, len(cardList)-0.5))
                currentCard = cardList.pop(rnd)
                playersCards[cardsToPlayer].append(currentCard)

    rnd = round(random.uniform(-0.49, len(cardList)-0.5))
    initialCard = cardList.pop(0)

    while initialCard[0] == "special" and initialCard[1] == "wild draw 4":
        cardList.append(initialCard)
        rnd = round(random.uniform(-0.49, len(cardList)-0.5))
        initialCard = cardList.pop(rnd)

    usedCards = [initialCard]

    return playerAmountList, playersCards, usedCards, cardList, playersPunctuation
