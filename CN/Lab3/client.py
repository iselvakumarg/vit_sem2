import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8995

# connection to hostname on the port.
s.connect((host, port))                               

# Get Input from the client
text = input("Enter the String: ")
s.send(text.encode())

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("The result got from the server is %s" % tm.decode())