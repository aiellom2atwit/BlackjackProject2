import os
import socket


def main():
    HOST = "localhost"
    PORT = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        # Create tcp connection with server address and port
        connection.connect((HOST, PORT))
        # initialzie the client loop
        initializeGame(connection)


def initializeGame(connection):
    # Asks user for name
    username = input(connection.recv(1024).decode())
    #If player doesn't input a name, refer to them as Player
    if (len(username) == 0):
        username = "Player"

    # Send username to server
    connection.send(username.encode())

    while True:
        # Display scoreboards
        os.system('cls' if os.name == 'nt' else 'clear')
        print(connection.recv(1024).decode())
        connection.send("[OK]".encode())

        serverMsg = connection.recv(1024).decode()

        
        if serverMsg.startswith("PLAYERS TURN"):
            # Player turn
            while True:
                hitCard = input("Hit a card? [Y/n]: ")

                if hitCard in ["", "y", "Y"]:
                    hitCard = True
                elif hitCard in ["n", "N"]:
                    hitCard = False
                if type(hitCard) == bool:
                    break

            connection.send(str(hitCard).encode())

        elif serverMsg.startswith("DEALERS TURN"):
            # Dealer turn
            input("Press [Enter] to continue.")
            connection.send("[OK]".encode())

        else:
            # Not a player turn - end of round
            connection.send("[OK]".encode())
            print(connection.recv(1024).decode())
            while True:
                playNewGame = input("Do you want to keep playing? [Y/n]: ")
                if playNewGame in ["", "y", "Y"]:
                    playNewGame = True
                elif playNewGame in ["n", "N"]:
                    playNewGame = False
                if type(playNewGame) == bool:
                    break
            connection.send(str(playNewGame).encode())

            if not playNewGame:
                #terminate the client process
                exit(0)


if __name__ == "__main__":
    main()