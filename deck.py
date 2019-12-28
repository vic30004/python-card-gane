import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return self.ranks+" of "+self.suits


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+ card.__str__()
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand: 
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def add_card(self,card):
        pass

    def adjust_for_ace(self):
        pass