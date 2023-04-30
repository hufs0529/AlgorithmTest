import socket
import ssl
import json
import zlib
import logging

SERVER_ADDRESS = ('localhost', 5000)
BUFFER_SIZE = 2048

logging.basicConfig(filename='server.log', level=logging.DEBUG)

def handle_task(data):
    task = data['task']
    if task == 'ping':
        import subprocess
        domain = data['domain']
        ping_response = subprocess.Popen(['ping', '-c', '1', domain], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        ip_address = ping_response.split()[2][1:-1]
        return {'ip_address': ip_address}
    elif task == 'toggle_string':
        s = data['string']
        toggled_s = ''.join([c.upper() if c.islower() else c.lower() for c in s])
        return {'toggled_string': toggled_s}
    else:
        return {'error': 'Invalid task'}

def encrypt_data(data):
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
        logging.error(f"Error: {e}")
        return None

def start_server():
    print("Starting server...")
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen()

        with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
            print(f"Server started on {SERVER_ADDRESS}")
            while True:
                conn, addr = ssl_socket.accept()
                print(f"Connection from {addr}")
                try:
                    data = conn.recv(BUFFER_SIZE)
                    if data:
                        decrypted_data = decrypt_data(data)
                        decompressed_data = decompress_data(decrypted_data)
                        response = handle_task(decompressed_data)
                        compressed_response = compress_data(response)
                        encrypted_response = encrypt_data(compressed_response)
                        conn.sendall(encrypted_response)
                except Exception as e:
                    logging.error(f"Error: {e}")
                finally:
                    conn.close()

if __name__ == '__main__':
    start_server()
