import Graphics


class Player:
    name : str
    wins = 0

    hand = []
    gameIndex : int
    isDealer = False

    def __init__(self, name, gameIndex, isDealer):
        self.name = name
        self.wins = 0
        self.gameIndex = gameIndex
        self.isDealer = isDealer

    def getHandValue(self):
        totalValue = 0
        hasAce = False
        for card in self.hand:
            #Add card value to total value
            totalValue += card[0]
            #If card value = 1, player has ace
            if card[0] == 1:
                hasAce = True
        if totalValue < 12 and hasAce:
            #If player has 10 cards or less plus ace, ace counts for 11
            #1 value already added for ace, add 1 more
            totalValue += 10
        return totalValue

    def resetHand(self):
        self.hand = []

    def showHand(self):
        return Graphics.showHand(self)

    def addCard(self, card):
        self.hand.append(card)
        #Print game status in server view
        if not self.isDealer:
            print("GAME #" + str(self.gameIndex) + ":", self.name, "is drawing a card.", self.name, "now has", str(self.getHandValue()), "cards!")
        elif self.isDealer:
            print("GAME #" + str(self.gameIndex) + ": Dealer is drawing a card. Dealer now has", str(self.getHandValue()), "cards!")

    def canHit(self):
        return self.getHandValue() < 21

    def lost(self):
        return self.getHandValue() > 21