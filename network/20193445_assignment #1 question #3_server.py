import random
import socket

MAX_BYTES = 1024

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(1)
    print('Waiting for a client...')
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)

    # Generate random number between 1 and 10
    number = random.randint(1, 10)
    attempts = 5

    # Inform the client to start the game
    client_socket.sendall(b'Start guessing! You have 5 attempts.')
    while attempts > 0:
        data = client_socket.recv(MAX_BYTES)
        if data.decode() == 'start':
            continue  # Skip guess validation for the "start" message
        guess = int(data.decode())
        if guess == number:
            # Client guessed the number correctly
            msg = 'Congratulations you did it.'.encode()
            client_socket.sendall(msg)
            break
        elif guess < number:
            # Client guessed too small
            msg = 'You guessed too small!'.encode()
            client_socket.sendall(msg)
        else:
            # Client guessed too high
            msg = 'You guessed too high!'.encode()
            client_socket.sendall(msg)
        attempts -= 1
    else:
        # Client ran out of attempts
        msg = 'You lost. The number was {}.'.format(number).encode()
        client_socket.sendall(msg)
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    server()
