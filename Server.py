import socket
import threading

from Blackjack import Blackjack
import Graphics


def main():
    HOST = "localhost"
    PORT = 1234

    gameIndex : int

    print("Initializing Server...")

    # TCP Socket creation
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()

        print("Waiting for connections...")
        while True:
            print(f"Running threads: {threading.active_count() - 1}")
            gameIndex = threading.active_count()

            cs, addr = sock.accept()

            currentClient = threading.Thread(group=None, target=clientLoop, name=None, args=(cs, addr, gameIndex))
            currentClient.start()


def clientLoop(cs, addr, gameIndex):
    with cs:
        # Asks client for username
        cs.send(Graphics.header().encode())

        # Receives username from client
        username = cs.recv(1024).decode()

        # Initialize the game
        blackjackGame = Blackjack(username, gameIndex)

        # Starts Round
        while True:
            blackjackGame.startRound()
            player_turn = True
            # Main loop
            while True:
                # Sends Scoreboard
                cs.send(str(blackjackGame).encode())
                cs.recv(1024) 
                if player_turn:
                    # Asks if the player wants more cards
                    cs.send("PLAYERS TURN".encode())
                    if cs.recv(1024).decode() == "True":
                        if blackjackGame.drawCard(0):
                            continue
                    player_turn = False

                else:
                    #Dealer's turn
                    if blackjackGame.dealerHits():
                        cs.send("DEALERS TURN".encode())
                        cs.recv(1024)
                        
                        blackjackGame.drawCard(1)

                    else:
                        print("GAME #" + str(gameIndex) + ": ROUND OVER")
                        cs.send("ROUND OVER".encode())
                        cs.recv(1024)
                        if blackjackGame.dealerWins():
                            cs.send("You lost!".encode())
                            print("GAME #" + str(gameIndex) + ": Blackjack round concluded with", username + ". Dealer wins.")
                        else:
                            cs.send("You win!".encode())
                            print("GAME #" + str(gameIndex) + ": Blackjack round concluded with", username + ".", username, "wins.")
                        break

            # Asks if the player wants to play another round
            if cs.recv(1024).decode() == "False":
                break


if __name__ == "__main__":
    main()