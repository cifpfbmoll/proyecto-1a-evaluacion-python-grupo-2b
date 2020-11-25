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
            cardAmount = cardAmount + 1
        initCards = Card(color, 0)
        cardList.append([initCards.c, initCards.n])
        cardAmount = cardAmount + 1
        for card in doubleCards:
            for z in range(0, 2):
                initCards = Card(color, card)
                cardList.append([initCards.c, initCards.n])
                cardAmount = cardAmount + 1
    return cardList

def playerSetup():
    print("Cuántos jugadores?")
    playerAmount = int(input())

    return playerAmount

def randomCardDistribution():
    for roundsPerPlayer in range(len(playerSetup())):
        rnd = round(random.uniform(0, len(initiateCards())))
