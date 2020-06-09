#this is the client.

import socket

"""
What is a socket..???

A socket is an end point of comunication.
With a socket you send and recive data.
The socket it self is not the comunication,
it is the end point that sits at an Ip and a port
"""

ip = "169.254.82.155"
port = 5555
BUFFERSIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip,port))
#s.connect((socket.gethostname(),port))


# we will look for the message sent from the MyServer.py program

while True:
    
    full_msg = ""
    new_msg = True
    
    while True:
        msg = s.recv(BUFFERSIZE+8)
        if new_msg:
            msglen = int(msg[:BUFFERSIZE])
            print("new message length: " + str(msglen))
            new_msg = False

                  
        full_msg += msg.decode("utf-8")

        if len(full_msg)-BUFFERSIZE == msglen:
                  print("Full msg recvd")
                  print(full_msg[BUFFERSIZE:])
                  new_msg = True
                  full_msg = ""
                  
    print(full_msg)
