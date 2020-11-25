import random


class Card:
    def __init__(self, col, num):
        self.c = col
        self.n = num

def initiateCards():

    doubleCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "reverse", "draw two", "skip"]
    colors = ["red", "green", "blue", "yellow"]
    specialCards = ["wild", "wild draw 4"]
    cardList = []
    cardAmount = 0

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

def randomCardDistribution():
    playerAmountList = list(range(1, playerSetup() + 1))
    if len(playerAmountList) < 2 or len(playerAmountList) > 10:
        print("Error! Número de jugadores inválido! Deben ser más de 2 y como mucho, 10.")
    else:
        print(playerAmountList)
        cardList = initiateCards()
        print(cardList)
        playersCards = []
        for createList in playerAmountList:
            playersCards.append([])
        for cardsToDistribute in range(7):
            for cardsToPlayer in range(len(playerAmountList)):
                rnd = round(random.uniform(0, len(cardList)))
                currentCard = cardList.pop(-rnd)
                playersCards[cardsToPlayer].append(currentCard)
                print(playersCards)

randomCardDistribution()