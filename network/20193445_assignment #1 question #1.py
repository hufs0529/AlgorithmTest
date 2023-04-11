import socket

HOST = 'ip-api.com'
PORT = 80
parameters = {'fields': 'city,regionName,country,lat,lon', 'lang': 'fr'}
query_string = '&'.join([f'{key}={value}' for key, value in parameters.items()])
MESSAGE = f'GET /json/?{query_string} HTTP/1.1\r\nHost: ip-api.com\r\n\r\n'

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))
    # send the HTTP request
    s.sendall(MESSAGE.encode('utf-8'))
    # receive the response
    data = s.recv(4096)

print(data.decode('utf-8'))
