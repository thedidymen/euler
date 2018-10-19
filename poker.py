import random
import itertools

class Card:

    rank_names = {
      1: "Ace",
      2: "Two",
      3: "Three",
      4: "Four",
      5: "Five",
      6: "Six",
      7: "Seven",
      8: "Eight",
      9: "Nine",
      10: "Ten",
      11: "Jack",
      12: "Queen",
      13: "King",
      14: "Ace"
    }

    suit_names = {
      'S': "Spades",
      'H': "Hearts",
      'D': "Diamonds",
      'C': "Clubs",
    }

    name_ranks = {
      'J': 11,
      'Q': 12,
      'K': 13,
      'A': 14,
    }

    def __init__(self, suit, rank=None):
        if rank is None:
            self.suit, self.rank = Card.parse(suit)
        else:
            self.suit, self.rank = suit, rank
        if self.rank == 1:
            self.rank = 14

    @classmethod
    def parse(cls, card):
        card = card.strip()
        suit = card[-1]
        rank = card[:-1].strip()
        if suit in cls.suit_names and rank in cls.name_ranks or int(rank) in cls.rank_names:
            rank = cls.name_ranks[rank] if rank in cls.name_ranks else int(rank)
            return (suit, rank)
        else:
            raise ValueError("Given card did not conform to required format, eg 2H for 2 of hearts or AC for ace of clubs")

    def __repr__(self):
        return "{0}{1}".format(self.rank if 2 <= self.rank <= 10 else self.rank_name[0], self.suit)

    def __str__(self):
        return "{0} of {1}".format(self.rank_name, self.suit_name)

    @property
    def rank_name(self):
        return Card.rank_names[self.rank]

    @property
    def suit_name(self):
        return Card.suit_names[self.suit]

    @classmethod
    def full_deck(cls):
        return [cls(suit, rank) for suit in cls.suit_names.keys() for rank in range(1,14)]


class Hand:

    names = Card.rank_names.copy()
    names.update({
        15: 'High Card',
        16: 'Pair',
        17: 'Two Pair',
        18: 'Three of a kind',
        19: 'Straight',
        20: 'Flush',
        21: 'Full house',
        22: 'Four of a kind',
        23: 'Straight Flush'
    })

    def __init__(self, cards):
        self.cards = sorted(cards, key = lambda card: card.rank)
        self.suits = [card.suit for card in cards]
        self.different_suits = len(set(self.suits))

        self.ranks = [card.rank for card in cards]
        self.rank_counts = {rank: self.ranks.count(rank) for rank in set(self.ranks)}
        self.different_ranks = len(set(self.ranks))
        self.highest = max(self.ranks)
        self.lowest = min(self.ranks)

    def flush(self):
        return self.different_suits == 1

    def straight(self):
        return self.different_ranks == 5 and self.highest - self.lowest == 4 or sorted(self.ranks) == [2,3,4,5,14]

    def straight_flush(self):
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        return sorted(self.rank_counts.values()) == [1,4]

    def three_of_a_kind(self):
        return sorted(self.rank_counts.values()) == [1,1,3]

    def full_house(self):
        return sorted(self.rank_counts.values()) == [2,3]

    def two_pair(self):
        return sorted(self.rank_counts.values()) == [1,2,2]

    def one_pair(self):
        return sorted(self.rank_counts.values()) == [1,1,1,2]

    def value(self):
        return ' '.join(self.names[x] for x in self.sort_key())

    def high_cards(self):
        return reduce(lambda acc,cur: acc+cur, ([k]*v for v,k in sorted(((v,k) for k,v in self.rank_counts.iteritems()), reverse=True)))

    def sort_key(self):
        if self.straight_flush():
            return [23] + self.high_cards()
        elif self.four_of_a_kind():
            return [22] + self.high_cards()
        elif self.full_house():
            return [21] + self.high_cards()
        elif self.flush():
            return [20] + self.high_cards()            
        elif self.straight():
            return [19] + self.high_cards()
        elif self.three_of_a_kind():
            return [18] + self.high_cards()
        elif self.two_pair():
            return [17] + self.high_cards()
        elif self.one_pair():
            return [16] + self.high_cards()
        else:
            return [15] + self.high_cards()


if __name__ == '__main__':
    deck = Card.full_deck()
    print deck[:13]
    print deck[13:26]
    print deck[26:39]
    print deck[39:]

    while True:
        choice = raw_input("enter a hand (Q to quit, R for random, H for help): ")
        if choice.lower() == 'q':
            break
        if choice.lower() == 'r':
            hand = Hand(random.sample(deck, 5))
        else:
            if choice.count(',') != 4:
                print 'Please enter a comma separated list of 5 cards as "rank suit", for example:'
                print '4H, 3D, 10S, KS, AS'
                hand = None
            else:
                hand = Hand([Card(card) for card in choice.split(',')])
        if hand:
            print hand.cards
            print "Best poker hand: {0}".format(hand.value())