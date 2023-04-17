import socket
import host_port

HOST = host_port.HOSTNAME
PORT = host_port.PORTNUMBER

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message to send (type 'quit' to exit): ")
        if message == 'quit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
print(data)
print('Connection closed.')
