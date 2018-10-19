__author__ = 'Reijer'

import random


handvalue = ["Royal Straight Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "One Pair", "High Card"]
cardsvalue = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
cardssuit = ('D', 'H', 'S', 'C')
allhands = ['8C TS KC 9H 4S', '8C TS 9C 8H 4S', '8C TS TC 8H 4S', '8C 8S TC 8H 4S', '2C 3S 4C 5H 6S', 'AC 2S 3C 4H 5S', '8D TD KD 9D 4D' ,'8C TS TC 8H 8S', '8C 8D TC 8H 8S', '9D TD JD QD KD', 'AC 2C 3C 4C 5C', 'TD JD QD KD AD']



def dealcard(deck):
    card = random.choice(cardsvalue)+random.choice(cardssuit)
    if card not in deck:
        deck.append(card)
        yield card


def main():
    deck = []




if __name__ == '__main__':
    main()