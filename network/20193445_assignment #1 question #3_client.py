import socket

MAX_BYTES = 1024  # Maximum number of bytes that can be received in a single transmission


def client():
    # Sets up a TCP client that connects to the server on localhost port 8888
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))
    print('Connected to server.')

    # Sends a "start" message to the server to begin the game
    client_socket.sendall(b'start')
    data = client_socket.recv(MAX_BYTES)
    print(data.decode())

    # Asks the user to guess a number between 1 and 10, and sends the guess to the server
    # The game allows for up to 5 attempts to guess the correct number
    attempts = 5
    while attempts > 0:
        guess = input('Guess a number between 1 and 10: ')
        try:
            guess = int(guess)
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 10.')
            continue
        client_socket.sendall(str(guess).encode())
        data = client_socket.recv(MAX_BYTES)
        print(data.decode())
        if 'Congratulations' in data.decode():
            # Client guessed the correct number and wins the game
            break
        attempts -= 1
    else:
        # Client ran out of attempts and loses the game
        print('You lost.')
    client_socket.close()

if __name__ == '__main__':
    client()
