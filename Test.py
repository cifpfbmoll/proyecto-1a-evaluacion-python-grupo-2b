import random
import math

class Card:
    def __init__(self, col, num):
        self.c = col
        self.n = num

class Player:
    def __init__(self, position, cards, score):
        self.pos = position
        self.cards = cards
        self.score = score

def initiateCards():

    doubleCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Reverse", "Draw 2", "Skip"]
    colors = ["Red", "Green", "Blue", "Yellow"]
    specialCards = ["Wild", "Wild draw 4"]
    cardList = []

    for color in colors:
        for specialCard in specialCards:
            initCards = Card("Special", specialCard)
            cardList.append(initCards)
        initCards = Card(color, 0)
        cardList.append(initCards)
        for card in doubleCards:
            for z in range(0, 2):
                initCards = Card(color, card)
                cardList.append(initCards)

    return cardList

def askForPlayers():
    print("Cuántos jugadores hay?")
    playerAmount = int(input())

    if 2 > playerAmount < 10:
        print("Deben ser al menos 2 jugadores y máximo 10")
        print("Cuántos jugadores hay?")
        playerAmount = int(input())

    return playerAmount

def cardsToPlayers(cardList, playerAmount):

    cardsForPlayers = []

    for playerAmount in range(playerAmount):
        cardsForPlayers.append([])

    for rounds in range(7):
        for listNumber in range(playerAmount+1):
            randomCard = math.floor(random.uniform(0, len(cardList)))
            cardToDistribute = cardList.pop(randomCard)
            cardsForPlayers[listNumber].append(cardToDistribute)

    return cardsForPlayers, cardList

def playerSetup(playerAmount):

    Players = []
    for position in range(1, playerAmount + 1):
        initPlayer = Player(position=position, cards=[], score=0)
        Players.append(initPlayer)

    return Players

def dropFirstCard(cardList):
    usedCards = []
    randomCard = math.floor(random.uniform(0, len(cardList)))
    usedCards.append(randomCard)

    return cardList


def giveCardsToPlayers(Players):
    cardDeck = initiateCards()
    for player in Players:
        print(player.pos)
        player.cards = ((cardsToPlayers(cardDeck, playerAmount))[(player.pos-1)])

    return Players

playerAmount = askForPlayers()