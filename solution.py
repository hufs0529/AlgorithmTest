import socket
import ssl
import json
import gzip
import threading
import logging

def handle_ping_task(data):
    domain = data['domain']
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "Unable to resolve domain"
    response = {'ip': ip}
    return response

def handle_toggle_string_task(data):
    string = data['string']
    toggled_string = ""
    for char in string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char
    response = {'toggled_string': toggled_string}
    return response

def handle_client(client_socket, client_address):
    try:
        logging.info(f"New client connected from {client_address}")
        while True:
            # Receive encrypted data
            encrypted_data = client_socket.recv(1024)
            
            # Decrypt data
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
            decrypted_data = context.decrypt(encrypted_data)
            
            # Decompress data
            decompressed_data = gzip.decompress(decrypted_data)
            
            # Decode JSON data
            data = json.loads(decompressed_data)
            
            # Handle task
            if data['task'] == 'ping':
                response = handle_ping_task(data)
            elif data['task'] == 'toggle_string':
                response = handle_toggle_string_task(data)
            else:
                response = {'error': 'Invalid task'}
            
            # Encode response as JSON
            response_json = json.dumps(response).encode('utf-8')
            
            # Compress response
            compressed_data = gzip.compress(response_json)
            
            # Encrypt response
            encrypted_data = context.encrypt(compressed_data)
            
            # Send response
            client_socket.sendall(encrypted_data)
    except (ConnectionResetError, ssl.SSLError):
        logging.info(f"Client disconnected from {client_address}")

def main():
    # Set up SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    
    # Set up socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket = context.wrap_socket(server_socket, server_side=True)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()
    
    # Handle clients
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    logging.basicConfig(filename='server.log', level=logging.INFO)
    main()
