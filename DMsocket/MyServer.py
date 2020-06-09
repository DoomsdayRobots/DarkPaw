#this is the server.

import socket
import time

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
s.bind((ip,port))
#s.bind((socket.gethostname(),port))

"""
Now its time to listen...
This is our server and because of that,
we are going to be making some connections to this server.
this server has to be prepaired for these incomming connections
Our server will handel a cue of 5 possible connections.
"""

s.listen(5)

while True:
    """
    so we are going to set our server up so that it will
    accept any and all incomming comunication connections.
    when some one finally dose connect this is what we will do...

    we will display their ip and port that they are connecting from.
    This is a way of being able to tell who is who
    and who we might be sending things back to.
    later we will use this as a way to be able to dectect
    a possible user and be able to choose what we send to that user.
    like an instant messageing service...
    
    Bob only gets bob's messages for Bob.
    Bob dose not recive messages meant for Janice.
    Janice can message Bob, and Bob can Message Janice.
    """
    
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")


    
    """
    lets send something back to the person
    who just connected to our server.
    """

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{BUFFERSIZE}}" + msg
    
    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"the time is! {time.time()}"
        msg = f"{len(msg):<{BUFFERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))
        
    #clientsocket.close()
        
