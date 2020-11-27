__author__ = 'Reijer'

import requests

cardsvalue = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
cardssuit = ('D', 'H', 'S', 'C')
allhands = ['8C TS KC 9H 4S', '8C TS KC 8H 4S', '8C TS 4C 8H 4S', '8C 8S TC 8H 4S', '2C 3S 4C 5H 6S', 'AC 2S 3C 4H 5S', '8D TD KD 9D 4D' ,'8C TS TC 8H 8S', '8C 8D TC 8H 8S', '9D TD JD QD KD', 'AC 2C 3C 4C 5C', 'TD JD QD KD AD']

def hands():
    r = requests.get('http://projecteuler.net/project/resources/p054_poker.txt')
    if not r:
        raise Exception
    for i in r.text.split('\n'):
        if i != "":
            yield str(i[:14]), str(i[15:])

def freq(hand):
    suit, value = {}, {}
    for x in hand:
        if x == " ":
            pass
        elif x not in cardssuit and x not in cardsvalue:
            print 'Error: invalid card input, use correct format'
        if x in cardssuit:
            suit[x] = suit.get(x,0) + 1
        elif x in cardsvalue:
            value[x] = value.get(x,0) + 1
    return suit, value

def flush(suit):
    return len(suit) == 1

def straight(value):
    if len(value) != 5:
        return False
    value = sorted(value, key=lambda x: cardsvalue.index(x))
    if value == ["2", "3", "4", "5", "A"]:
        return True
    indextor = cardsvalue.index(value[0])
    return tuple(value) == cardsvalue[indextor: indextor+5]

def kind(value, n):
    return any(x == n for x in value.values())

def twopair(value):
    x = sorted(value.values()) == [1, 2, 2]
    return x

def highcards(value):
    if value == None:
        return None
    return sorted(value, key=lambda x: cardsvalue.index(x))

def hit(hand):
    suit, value = freq(hand)
    sortedvalue = sorted(value, key=lambda x: cardsvalue.index(x))
    # hitlist = flush, straight, four of kind, three of kind, two pair, pair"
    hitlist = [flush(suit), straight(value), kind(value, 4), kind(value, 3), twopair(value), kind(value, 2)]
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if hitlist == [True, True, False, False, False, False] and sortedvalue[-2] == "K":
        return "Royal Straight Flush", None, None
    # Straight Flush: All cards are consecutive values of same suit.
    elif hitlist == [True, True, False, False, False, False]:
        return "Straight Flush", [sortedvalue[-1]], None
    # Four of a Kind: Four cards of the same value.
    elif hitlist == [False, False, True, False, False, False]:
        return "Four of a Kind", [k for k, v in value.items() if v == 4], [k for k, v in value.items() if v == 1]
    # Full House: Three of a kind and a pair.
    elif hitlist == [False, False, False, True, False, True]:
        return "Full House", [k for k, v in value.items() if v == 3]+[k for k, v in value.items() if v == 2], None
    # Flush: All cards of the same suit.
    elif hitlist == [True, False, False, False, False, False]:
        return "Flush", [sortedvalue[-1]], None
    # Straight: All cards are consecutive values.
    elif hitlist == [False, True, False, False, False, False]:
        return "Straight", [sortedvalue[-1]], None
    # Three of a Kind: Three cards of the same value.
    elif hitlist == [False, False, False, True, False, False]:
        return "Three of a Kind", [k for k,v in value.items() if v == 3], [k for k,v in value.items() if v == 1]
    # Two Pairs: Two different pairs.
    elif hitlist == [False, False, False, False, True, True]:
        return "Two Pair", [k for k, v in value.items() if v == 2], [k for k, v in value.items() if v == 1]
    # One Pair: Two cards of the same value.
    elif hitlist == [False, False, False, False, False, True]:
        return "One Pair", [k for k, v in value.items() if v == 2], [k for k, v in value.items() if v == 1]
    # High Card: Highest value card.
    else:
        return "High Card", [k for k, v in value.items() if v == 1], None

def showdown(player1, player2):
    pl1hand, pl1handvalue, pl1kicker = hit(player1)
    pl2hand, pl2handvalue, pl2kicker = hit(player2)
    cardranks = ["Royal Straight Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pair", "One Pair", "High Card"]
    if cardranks.index(pl1hand) < cardranks.index(pl2hand):
        return "player 1"
    elif cardranks.index(pl1hand) > cardranks.index(pl2hand):
        return "player 2"
    else:
        "high card stuff"


def main():
    for i,j in hands():
        print showdown(i, j)


    # for i in allhands:
    #     print i,
    #     showdown, internal, kicker = hit(i)
    #     print showdown, highcards(internal), highcards(kicker)




if __name__ == '__main__':
    main()