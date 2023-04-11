import socket

MAX_BYTES = 65535  # Maximum number of bytes that can be received in a single datagram
KEY = 3  # Number of positions by which each character in the message is shifted during encryption


def decrypt(data):
    # Decrypts an encrypted string by shifting each character by KEY positions
    return ''.join([chr((ord(c) - KEY) % 256) for c in data])


def client(ip, port, message):
    # Sets up a UDP client that sends a message to the specified IP and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = message.encode('ascii')
    sock.sendto(message, (ip, port))
    try:
        # Waits for a response from the server, then decrypts and displays it
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        decrypted_text = decrypt(text)
        print('The server at {} replied {!r}'.format(address, decrypted_text))
    except ConnectionResetError:
        print('Connection reset by peer')

if __name__ == '__main__':
    server_port = 1060
    message = 'Hello, world!'
    client_ip = '127.0.0.1'
    client(client_ip, server_port, message)