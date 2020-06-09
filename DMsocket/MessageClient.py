import socket
import select
import errno
import sys

HEADDER_LENGTH = 80

IP = "169.254.82.155"
PORT = 5555
my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP,PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode("utf-8")
username_headder = f"{len(username):<{HEADDER_LENGTH}}".encode("utf-8")
client_socket.send(username_headder + username)

# we want to both send messages and receive messages
while True:
    message = input(f"{my_username} > ")
    #message = ""

    if message:
        message = message.encode("utf-8")
        message_headder = f"{len(message):<{HEADDER_LENGTH}}".encode("utf-8")
        client_socket.send(message_headder + message)

    try:
        while True:
            # receive things
            username_headder = client_socket.recv(HEADDER_LENGTH)
            if not len(username_headder):
                print("Connection closed by the server")
                sys.exit()
                
            # Convert headder to int value    
            username_length = int(username_headder.decode("utf-8").strip())

            # receive and decode username
            username = client_socket.recv(username_length).decode("utf-8")

            # Now do the same for message(as we received username, we received whole message, there's no need to check if it has any length)
            message_headder = client_socket.recv(HEADDER_LENGTH)
            message_length = int(message_headder.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            # Print the message
            print(f"{username} > {message}")
            
    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Reading erroe",str(e))
            sys.exit()
            
        # We just did not receive anything    
        continue
                
    except Exception as e:
        # Any other exception - something happened, exit
        print("General error",str(e))
        sys.exit()
        
        
    
