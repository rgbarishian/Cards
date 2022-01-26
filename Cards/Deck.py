import random


class Card():
    def __init__(self, suit, value):
        self.suite = suit
        self.value = value

    def list(self):
        return(f'{self.value} of {self.suite}')
    
    def short_show(self):
        return(f'{self.suite[0]}{self.value}')
    
    def long_show(self):
        return(f'{self.suite}{self.value}')
    
    def get_value(self):
        return self.value

class Deck():
    '''
    class: Deck object of Cards

    Attributes:
        cards: LIst of Cards in desk
    '''
    def __init__(self, num_decks=1):
        self.cards = []
        self._build_deck(num_decks)

    def _build_deck(self, number_of_decks):
        values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for deck_num in range(number_of_decks):
            for suit in suits:
                for value in values:
                    self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, number):
        dealt = []
        for i in range(number):
            dealt.append(self.cards.pop(0))
        return dealt

    def show(self):
        for card in self.cards:
            print(card.short_show())