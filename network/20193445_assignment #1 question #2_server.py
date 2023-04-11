import socket

MAX_BYTES = 65535
KEY = 3  # Number of positions by which each character in the message is shifted during encryption

def encrypt(data):
    # Encrypts a string by shifting each character by KEY positions
    return ''.join([chr((ord(c) + KEY) % 256) for c in data])

def encrypt(message):
    encrypted_message = ""
    for c in message:
        if c.isalpha():
            if c.lower() == 'z':
                encrypted_message += 'a'
            else:
                encrypted_message += chr(ord(c.lower()) + 1)
        else:
            encrypted_message += c
    return encrypted_message
  
def server(port):
    # Sets up a UDP server that listens for incoming datagrams on the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        # Waits for a datagram to arrive, then decrypts it and sends it back to the client
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        encrypted_text = encrypt(text)
        data = encrypted_text.encode('ascii')
        sock.sendto(data, address)
        
if __name__ == '__main__':
    server_port = 1060
    server(server_port)