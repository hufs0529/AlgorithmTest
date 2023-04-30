import socket
import ssl
import json
import zlib

SERVER_ADDRESS = ('localhost', 5000)
BUFFER_SIZE = 2048

def encrypt_data(data):
    if isinstance(data, bytes):
        return data
    else:
        return data.encode('utf-8')

def decrypt_data(data):
    return data.decode('utf-8')

def compress_data(data):
    return zlib.compress(json.dumps(data).encode('utf-8'))

def decompress_data(data):
    try:
        decompressed_data = zlib.decompress(data, wbits=zlib.MAX_WBITS | 16)
        return decompressed_data.decode('utf-8')
    except zlib.error as e:
        return None



def start_client():
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = ssl.wrap_socket(ssock, cert_reqs=ssl.CERT_NONE)
    sock.connect(SERVER_ADDRESS)
    print(f"Connected to {SERVER_ADDRESS}")

    while True:
        task = input("Enter task (ping/toggle_string): ")
        if task == 'ping':
            domain = input("Enter domain: ")
            query = {'task': 'ping', 'domain': domain}
        elif task == 'toggle_string':
            s = input("Enter string: ")
            query = {'task': 'toggle_string', 'string': s}
        else:
            print("Invalid task")
            continue

        compressed_query = compress_data(query)
        encrypted_query = encrypt_data(compressed_query)

        sock.sendall(encrypted_query)

        response = sock.recv(BUFFER_SIZE)
        decrypted_response = decrypt_data(response)
        decompressed_response = decompress_data(decrypted_response)

        print(decompressed_response)

    sock.close()

if __name__ == '__main__':
    start_client()
