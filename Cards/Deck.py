from collections import deque
import random

class Card():
    '''Creates card object
    Builds card object with suit and value

    Attributes:
        suit: A string indicating the suit of the card
        value: A string/integer indicating the suit of the card
    '''

    def __init__(self, suit, value):
        ''' Initialize Card object with suit and value'''
        if suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            self._suit = suit
        else:
            raise ValueError(f'Suit {suit} does not match any \'Clubs\', \'Diamonds\', \'Hearts\', \'Spades\'')
        if value in [2,3,4,5,6,7,8,9,10,'J','Q','K','A']:
            self._value = value
        else:
            raise ValueError(f'Value {value} does not match any \'2,3,4,5,6,7,8,9,10,J,Q,K,A]\'')

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    @property
    def fcard(self):
        '''Full state of card in verbal format
        ie \'Three of Spades\'
        '''
        return(f'{self._value} of {self._suit}')
    
    @property
    def scard(self):
        '''Card in short form
        2 of Hearts will return as H2
        '''
        return(f'{self._suit[0]}{self._value}')
    
    @property
    def lcard(self):
        '''Card in long form
        2 of Hearts will return as Hearts2
        '''
        return(f'{self._suit}{self._value}')
    
    @property
    def score(self):
        '''Score, similar to value but gives face cards numeric value
        2-10 have standard values J=11, Q=12, K=13, A=14
        ADD OPTION TO GIVE ACE VALUE OF 1 OR 14
        '''
        conversion = {'J':11,'Q':12,'K':13,'A':14}
        if isinstance(self._value, int):
            return self._value
        return conversion[self._value]

class Deck():
    '''Deck object of Cards
    Top of deck is left side of deque while bottom is right side
    A deque is used so dealing from the bottom is technically possible
    Decks are dealt from the top by default

    Attributes:
        cards: Deque of Cards in desk
    '''
    def __init__(self, num_decks=1):
        self.deck = deque([])
        
        self._build_deck(num_decks)

    @property
    def sdeck(self):
        '''Deque of cards in short form
        ie deque(['H2','S5','CK'])
        '''
        sdeck = deque()
        for card in self.deck:
            sdeck.append(card.scard)
        return sdeck

    def __len__(self):
        return len(self.sdeck)

    def _build_deck(self, number_of_decks):
        '''Builds list cards

        Args:
            number_of_decks: An integer that tells how many standard (52 card)
                decks to make
        '''
        values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for deck_num in range(number_of_decks):
            for suit in suits:
                for value in values:
                    self.deck.append(Card(suit, value))
    
    def shuffle(self, seed=None):
        '''Shuffles deck into random order

        Args:
            seed: Integer seed for random number generator
        '''
        random.Random(seed).shuffle(self.deck)
    
    def deal(self, number):
        '''Removes certain number of consecutive cards in deck and returns

        Args:
            number: An integer that tells how many cards to deal
        
        Returns:
            A card object pulled from the top of the deck
        '''
        ##Need to add check if there are more cards requested than left in deck
        dealt = []
        for i in range(number):
            dealt.append(self.deck.popleft())
        return dealt

class CardSet():
    '''Abstract Object for any set of Cards
    Deck and hands will inherit from this class

    Attributes:
        cards: List of Cards in desk
    '''
    def __init__():
        pass