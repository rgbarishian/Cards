from collections import deque
import unittest

from Cards import Card, Deck

class testCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card('Spades', 2)

    def test_value(self):
        self.assertEqual(self.card.value,2)
    
    def test_suit(self):
        self.assertEqual(self.card.suit, 'Spades')

    def test_fcard(self):
        self.assertEqual(self.card.fcard, '2 of Spades')
    
    def test_scard(self):
        self.assertEqual(self.card.scard, 'S2')

    def test_lcard(self):
        self.assertEqual(self.card.lcard, 'Spades2')

class testDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck(1)
    
    def test_deck_length(self):
        self.assertEqual(len(self.deck.deck), 52)
    
    def test_deck_length_one_removed(self):
        self.deck.deck.pop()
        self.assertEqual(len(self.deck.deck), 51)
    
    def test_sdeck_length(self):
        self.assertEqual(len(self.deck.deck), 52)
    
    def test_sdeck_length_one_removed(self):
        self.deck.deck.pop()
        self.assertEqual(len(self.deck.sdeck), 51)
    
    def test_deal_one(self):
        card = self.deck.deal(1)
        self.addTypeEqualityFunc(Card, self.are_elements_equal)
        self.assertEqual(card[0], Card('Clubs',2))
    
    def test_deal_two(self):
        cards = self.deck.deal(2)
        self.assertEqual(len(cards), 2)
        self.addTypeEqualityFunc(Card, self.are_elements_equal)
        self.assertEqual(cards[0], Card('Clubs',2))
        self.assertEqual(cards[1], Card('Clubs',3))
    
    def test_shuffle(self):
        original = self.deck.sdeck
        self.deck.shuffle(231)
        self.assertNotEqual(self.deck.sdeck, original)
        shuffled = deque(['H7', 'CJ', 'C8', 'C6', 'S8', 'H6', 'HJ', 'D4', 'H3',
            'S4', 'C7', 'SQ', 'H9', 'C4', 'DQ', 'C5', 'D5', 'HA', 'S3', 'S9', 
            'H10', 'HK', 'H8', 'CA', 'S6', 'DA', 'D10', 'H4', 'C2', 'CK', 'SK',
            'D6', 'DJ', 'CQ', 'SA', 'S2', 'C9', 'S5', 'D7', 'S7', 'SJ', 'H5',
            'H2', 'D8', 'S10', 'D2', 'D3', 'HQ', 'D9', 'DK', 'C10', 'C3'])
        self.assertEqual(self.deck.sdeck, shuffled)

    def are_elements_equal(self, first_element, second_element, msg=None):
        self.assertEqual(type(first_element), type(second_element))
        try:
            type(vars(first_element)) is dict
        except:
            self.assertEqual(first_element, second_element)
        else:
            for i in vars(first_element).keys():
                try:
                    type(vars(vars(first_element)[i])) is dict
                except:
                    if type(vars(first_element)[i]) is list:
                        for j in range(len(vars(first_element)[i])):
                            self.are_elements_equal(vars(first_element)[i][j], vars(second_element)[i][j])
                    else:
                        self.assertEqual(vars(first_element)[i], vars(second_element)[i])
                else:
                    self.are_elements_equal(vars(first_element)[i], vars(second_element)[i])

if __name__ == '__main__':
    unittest.main()
