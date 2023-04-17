import socket
import host_port

HOST = host_port.HOSTNAME
PORT = host_port.PORTNUMBER

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # CONNECTION
    s.connect((HOST, PORT))

    # INPUTS
    op = input("Enter operator (+, -, *, /): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # SEND TO SERVER
    s.sendall(f"{op} {num1} {num2}".encode())

    # RECEIVE FROM SERVER
    data = s.recv(1024)

print('Result:', data.decode())
