from collections import deque
import unittest

from Cards import Card, Player

class testPlayerConstants(unittest.TestCase):
    def setUp(self):
        self.player = Player('Test-Name')

    def test_name(self):
        self.assertEqual(self.player.name, 'Test-Name')

class testPlayerCards(unittest.TestCase):
    def setUp(self):
        self.player = Player('Test-Name')
        self.cards = deque([Card('Spade','Ace'), Card('Hearts',2), Card('Diamonds',9)])
        self.receive(self.cards)

    
class testPlayerActions(unittest.TestCase):
    def setUp(self):
        self.player = Player('Test-Name')
    
    def test_deck_receive_one_card(self):
        card = Card('Spades','A')
        self.player.receive(deque([card]))
        self.addTypeEqualityFunc(Card, self.are_elements_equal)
        self.assertEqual(self.player.hand[0], card)

    def test_deck_receive_two_cards(self):
        card1 = Card('Spades','A')
        card2 = Card('Hearts', 4)
        self.player.receive(deque([card1, card2]))
        self.addTypeEqualityFunc(Card, self.are_elements_equal)
        self.assertEqual(self.player.hand[0], card2)
        self.assertEqual(self.player.hand[1], card1)

    def test_deck_play_cards(self):
        card = Card('Spades','A')
        self.player.receive(deque([card]))
        self.addTypeEqualityFunc(Card, self.are_elements_equal)
        self.assertEqual(self.player.hand[0], card)

        played = self.player.play('SA')
        self.assertEqual(played, card)

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