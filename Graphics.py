
#Contains the text graphics for Blackjack

def header():
    return '''\
++++++++++++++++++++++++++++++++++
       Welcome to Blackjack!       
++++++++++++++++++++++++++++++++++

Enter a username: '''


def scoreboard(players):
    message = '''\
++++++++++++++++++++++++++++++++++
            Scores
----------------------------------
'''
    for player in players:
        message += f"{player.name}: {player.wins}\n"
    message += '''\
----------------------------------
'''
    for player in players:
        message += f"{player.showHand()}\n"
    message += '''\
++++++++++++++++++++++++++++++++++

'''
    return message


def showHand(player):
    message = f'''
Player    : {player.name}
Hand Value: {player.getHandValue()}
Cards     :'''
    for card in player.hand:
        message += (f" {card[1]}")
    message += "\n"
    return message


def playerLost():
    return '''\
++++++++++++++++++++++++++++++++++
             You win!
++++++++++++++++++++++++++++++++++
'''


def playerWon():
    return '''\
++++++++++++++++++++++++++++++++++
            You lost!
++++++++++++++++++++++++++++++++++
'''