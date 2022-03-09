import math

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
            #find better way to write this
            # needs to constant loop so subsequent wars can be run automatically
            #setup table where cards are being played
            self.table = {i.name:[] for i in self.players}

            #play hand
            for player in self.players:
                self.table[player.name].append(player.play())
            winner_index = self._score_hand()
            if len(winner_index)>1:
                # Make sure everyone has at least 4 cards, if not adjust number of cards used in war
                number_down = 4
                for index in winner_index:
                    player = self.players[index]
                    if len(player.shand) < 4:
                        number_down = len(player.shand)
                
                for index in winner_index:
                    player = self.players[index]
                    for down in range(number_down):
                        self.table[player.name].append(player.play())
                
                winner_index = self._score_hand()
                print('x')

            else:
                winner_name = list(self.table.keys())[winner_index[0]]
                for player in self.players:
                    if player.name == winner_name:
                        #gather cards from table and put in players discard pile
                        player.receive_discard(i[0] for i in self.table.values())
                        break

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
            # top_score = 
            #if tied, call a war or if someone wins, 

    def _score_hand(self):
        scores = np.array([i[-1].score for i in self.table.values()])
        winner_index = np.where(scores==max(scores))[0]
        return winner_index

    def _execute_war(self):
        pass

    def war(self):
        pass

    def end_game(self):
        print(f'Game Ends\n{self.players[0].name} Wins!')

if __name__ == '__main__':
    game = War(1)
    game.add_player('George')
    game.add_player('Ryan')
    
    game.deal()
    game.quick_play()

    pass