import socket
import host_port

HOST = host_port.HOSTNAME
PORT = host_port.PORTNUMBER

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break
            values = data.decode().split()
            op = values[0]
            num1 = int(values[1])
            num2 = int(values[2])

            # GENERAL IF ELSE 
            # if op == '+':
            #     result = num1 + num2
            # elif op == '-':
            #     result = num1 - num2
            # elif op == '*':
            #     result = num1 * num2
            # elif op == '/':
            #     result = num1 / num2
            # else:
            #     result = 'Invalid operator'

            # MATCH CASE
            match op:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    result = num1 / num2
                case _:
                    result = 'Invalid operator'

            conn.sendall(str(result).encode())
