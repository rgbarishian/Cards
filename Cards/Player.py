from collections import deque
import random

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = deque()
        self.discard = deque()
        self.visible = deque
    
    @property
    def shand(self):
        shand = deque()
        for card in self.hand:
            shand.append(card.scard)
        return shand
    
    @property
    def lhand(self):
        lhand = deque()
        for card in self.hand:
            lhand.append(card.lcard)
        return lhand
    
    @property
    def sdiscard(self):
        sdiscard = deque()
        for card in self.discard:
            sdiscard.append(card.scard)
    
    @property
    def ldiscard(self):
        ldiscard = deque()
        for card in self.discard:
            ldiscard.append(card.lcard)
    
    def receive(self, cards, visible=False):
        self.hand.extendleft(cards)
        if visible:
            self.visible.extendleft(cards)

    def receive_discard(self, cards):
        self.discard.extendleft(cards)

    def play(self, val=None):
        '''
        '''
        if val:
            if len(val) == 2:
                suit, value = self._convert(val)
            else:
                suit, value = val[0], val[1]
            for card in self.hand:
                if card.suit == suit and card.value == value:
                    self.hand.remove(card)
                    return card
        else:
            return self.hand.popleft()

    def shuffle_hand(self, seed=None):
        random.Random(seed).shuffle(self.hand)

    def shuffle_discard(self, seed=None):
        random.Random(seed).shuffle(self.discard)

    def disc_to_hand(self, shuffle='After', seed=None):
        '''Moves discard cards to hand and shuffles if desired
        Args:
            shuffle:
                Options of 'Before', 'After', None to tell when or if to 
                shuffle cards
        '''
        if shuffle=='Before':
            self.shuffle_discard(seed)
        self.hand.extend(self.discard)
        self.discard.clear()
        if shuffle == 'After':
            self.shuffle_hand(seed)

    def _convert(self, card_string):
        '''Converts from scard to lcard length
        '''
        match card_string[0]:
            case 'H':
                suit = 'Hearts'
            case 'S':
                suit = 'Spades'
            case 'D':
                suit = 'Diamonds'
            case 'C':
                suit = 'Clubs'
        return suit, card_string[1]