import socket
import pickle


port = 1234
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))

while True:

    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv((HEADERSIZE+6))
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d=pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            
            new_msg = True
            full_msg = b""

    print(full_msg)


























    

