import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8995                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)

def checkVowel(vowel, word):
    count = 0
    for i in word:
        if i in vowel:
           count += 1 
    return str(count)                                          

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    clientStr = clientsocket.recv(1024)
    clientStr = clientStr.decode()
    
    res = checkVowel(vowelList, clientStr)
    
    clientsocket.send(res.encode())
    clientsocket.close()