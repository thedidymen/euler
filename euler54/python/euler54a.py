__author__ = 'Reijer'

import requests

handvalue = ["Royal Straight Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "One Pair", "High Card"]
cardsvalue = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
cardssuit = ('D', 'H', 'S', 'C')
allhands = ['8C TS KC 9H 4S', '8C TS 9C 8H 4S', '8C TS TC 8H 4S', '8C 8S TC 8H 4S', '2C 3S 4C 5H 6S', 'AC 2S 3C 4H 5S', '8D TD KD 9D 4D' ,'8C TS TC 8H 8S', '8C 8D TC 8H 8S', '9D TD JD QD KD', 'AC 2C 3C 4C 5C', 'TD JD QD KD AD']

def hands():
    r = requests.get('http://projecteuler.net/project/resources/p054_poker.txt')
    if not r:
        raise Exception
    for i in r.text.split('\n'):
        if i != "":
            yield str(i[:14]), str(i[15:])

def parsepokerhandformstupidtouseful(x):
    hand = [cards for cards in x.split(" ")]
    cards = [(card[0], card[1]) for card in hand]
    cards = sorted(cards, key=lambda x: cardsvalue.index(x[0]))
    value = [i[0] for i in cards]
    suit = [i[1] for i in cards]
    return value, suit


def straight(value):
    if len(value) != 5:
        return False
    if value == ["2", "3", "4", "5", "A"]:
        return True
    indextor = cardsvalue.index(value[0])
    return tuple(value) == cardsvalue[indextor: indextor+5]

def myhand(value, suit):
    if len(set(suit)) == 1:             #checks for (royal, straight) flush
        if straight(value):
            if value[0] == "T":         #Royal straight flush
                return [0, value]
            else:
                if value == ["2", "3", "4", "5", "A"]:
                    value = ["A", "2", "3", "4", "5"]
                return [1, value]       #straight flush
        else:
            return [4, value]           #Flush
    elif len(set(value)) == 5:          #checks for straight or high card
        if straight(value):
            if value == ["2", "3", "4", "5", "A"]:
                value = ["A", "2", "3", "4", "5"]
            return [5, value]           #Straight
        else:
            return [9, value]           #high card
    freq = {i:value.count(i) for i in set(value)}
    vl = []
    for i in range(0, 5):
        l = [j for j in freq if freq[j] == i]
        vl += sorted(l, key=lambda x: cardsvalue.index(x))
    freqlist = sorted(freq.values())
    if len(freq) > 2:                   #checks for one pair or two pair, three of a kind
        if freqlist == [1, 1, 1, 2]:    #one pair
            return [8, vl]
        elif freqlist == [1, 2, 2]:     #two pair
            return [7, vl]
        else:
            return [6, vl]              #three of a kind
    elif freqlist == [2, 3]:
        return [3, vl]                  #full house
    else:
        return [2, vl]                  #four of a kind

def compa(hand1, hand2):
    if hand1[0] != hand2[0]:
        return hand1[0] < hand2[0]
    for i in range(len(hand1[1])-1, -1, -1):
        if hand1[1][i] != hand2[1][i]:
            return cardsvalue.index(hand1[1][i]) > cardsvalue.index(hand2[1][i])
    return None

def main():
    pl1, pl2, total = 0, 0, 0
    for pl1hand, pl2hand in hands():
        total +=1
        pl1value, pl1suit = parsepokerhandformstupidtouseful(pl1hand)
        pl2value, pl2suit = parsepokerhandformstupidtouseful(pl2hand)
        pl1handvalue = myhand(pl1value, pl1suit)
        pl2handvalue = myhand(pl2value, pl2suit)
        print "Player 1:", handvalue[pl1handvalue[0]], "with", pl1handvalue[1][::-1]
        print "Player 2:", handvalue[pl2handvalue[0]], "with", pl2handvalue[1][::-1]
        if compa(pl1handvalue, pl2handvalue):
            print "Winner: Player 1"
            pl1 += 1
        elif compa(pl1handvalue, pl2handvalue) == None:
            print "Split pot"
        else:
            print "Winner: Player 2"
            pl2 += 1
    print "Player 1 won:", pl1, "times"
    print "Player 2 won:", pl2, "times"
    print "Splitpot:", total - pl1 - pl2, "times"
    print "Total:", total






if __name__ == '__main__':
    main()