
import random
from Player import Player
import Graphics


allCards = [(1, '🃁'), (1, '🂡'), (1, '🂱'), (1, '🃑'),
             (2, '🃂'), (2, '🂢'), (2, '🂲'), (2, '🃒'),
             (3, '🃃'), (3, '🂣'), (3, '🂳'), (3, '🃓'),
             (4, '🃄'), (4, '🂤'), (4, '🂴'), (4, '🃔'),
             (5, '🃅'), (5, '🂥'), (5, '🂵'), (5, '🃕'),
             (6, '🃆'), (6, '🂦'), (6, '🂶'), (6, '🃖'),
             (7, '🃇'), (7, '🂧'), (7, '🂷'), (7, '🃗'),
             (8, '🃈'), (8, '🂨'), (8, '🂸'), (8, '🃘'),
             (9, '🃉'), (9, '🂩'), (9, '🂹'), (9, '🃙'),
             (10, '🃊'), (10, '🂪'), (10, '🂺'), (10, '🃚'),
             (10, '🃋'), (10, '🂫'), (10, '🂻'), (10, '🃛'),
             (10, '🃍'), (10, '🂭'), (10, '🂽'), (10, '🃝'),
             (10, '🃎'), (10, '🂮'), (10, '🂾'), (10, '🃞')]

gameIndex : int

class Blackjack:
    def __init__(self, name, gameIndex):
        self.name = name
        self.gameIndex = gameIndex
        self.players = [Player(name, gameIndex, isDealer=False), Player('Dealer', gameIndex, isDealer=True)]

    def __repr__(self):
        return Graphics.scoreboard(self.players)

    def startRound(self):
        print("GAME #" + str(self.gameIndex) + ": Initializing new Blackjack round with", self.name)
        print("GAME #" + str(self.gameIndex) + ": Dealer Wins #:", self.players[1].wins, "     ", self.players[0].name, "Wins #:", self.players[0].wins)
        self.deck = allCards[:]
        for index, player in enumerate(self.players):
            player.resetHand()
            self.drawCard(index)

    def dealerHits(self):
        return (self.players[0].getHandValue() < 21 and not self.players[0].lost() and not self.players[1].lost() and self.players[0].getHandValue() >= self.players[1].getHandValue())

    def drawCard(self, player_id):
        player = self.players[player_id]
        player.addCard(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        return player.canHit()

    def dealerWins(self):
        if (self.players[0].lost() or (not self.players[1].lost() and (self.players[0].getHandValue() < self.players[1].getHandValue()))):
            self.players[1].wins += 1
            return True

        self.players[0].wins += 1
        return False

    def getDealerScore(self):
        return (self.players[0].getHandValue())

    def getGameIndex(self):
        return self.gameIndex