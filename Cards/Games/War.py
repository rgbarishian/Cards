from functools import reduce
import math
import operator

import numpy as np

from Cards import Deck, Player

class War():
    def __init__(self, num_decks):
        self.deck = Deck(num_decks)
        self.deck.shuffle()
        self.players = []
        self.current_play = {}

    def add_player(self, name):
        self.players.append(Player(name))
    
    def deal(self, num_each=None, at_a_time=1):
        '''Deals cards to each player
        If num_each is not declared, all cards are dealt
        Args:
            num_each: Number of cards to deal to each player
            at_a_time: Number of cards to deal to each player at a time
        '''
        if not num_each:
            num_each = math.ceil(len(self.deck)/len(self.players))
        while num_each:
            num_each-=1
            for player in self.players:
               player.receive(self.deck.deal(at_a_time))
    
    def quick_play(self):
        Game = True
        while Game == True:
            #setup table where cards are being played
            self.table = {i.name:[] for i in self.players}

            #play hand
            for player in self.players:
                self.table[player.name].append(player.play())
            winner_index = self._score_hand()

            #If there is a tie, fall into a war loop
            while len(winner_index) != 1:
                # Make sure everyone has at least 4 cards
                # if not add discard back to hand
                # if still not adjust number of cards used in war
                print('WAR')
                number_down = 4
                for index in winner_index:
                    player = self.players[index]
                    if len(player.hand) < 4:
                        player.disc_to_hand(shuffle='Before')
                        if len(player.hand) < 4:
                            number_down = len(player.hand)
                
                for index in winner_index:
                    player = self.players[index]
                    for down in range(number_down):
                        self.table[player.name].append(player.play())
                
                winner_index = self._score_hand()

            #find winner of hand
            winner = self.players[winner_index[0]]
            #flattens list of values lists to single list
            table_cards = reduce(operator.concat, self.table.values())
            #give cards on table to winner
            winner.receive_discard(table_cards)
            
            #check if player is out of hand
            for player in self.players:
                if not player.hand:
                    if not player.discard:
                        self.players.remove(player)
                        if len(self.players) == 1:
                            self.end_game()
                            Game = False
                    else:
                        player.disc_to_hand()

    def _score_hand(self):
        scores = np.array([i[-1].score for i in self.table.values()])
        winner_index = np.where(scores==max(scores))[0]
        return winner_index

    def end_game(self):
        print(f'Game Ends\n{self.players[0].name} Wins!')

if __name__ == '__main__':
    game = War(1)
    game.add_player('George')
    game.add_player('Ryan')
    
    game.deal()
    game.quick_play()

    pass