import socket
import time
import pickle


"""
Sockets are a way of transmitting data,
they them selves are not the form of communication.
the socket sits at an IP address in a port.

the 1234 is the port number the smaller the number, the
higher the chances are thst some one else is using it

we have a listener que of 5 
"""

port = 1234
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")


    d = {1: "Hey", 2: "Their"}
    msg = pickle.dumps(d)
    print(msg)

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    clientsocket.send(msg)


    

    """
    msg = "Welcome to the server!\n"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg

    clientsocket.send(bytes(msg,"utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}\n"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg,"utf-8"))
    """

   

















        

        
