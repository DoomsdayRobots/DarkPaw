import socket
import select

HEADDER_LENGTH = 80
IP = "169.254.82.155"
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_socket.bind((IP,PORT))
server_socket.listen()


sockets_list = [server_socket]
clients = {}

def receive_message(client_socket):
    try:
        message_headder = client_socket.recv(HEADDER_LENGTH)

        if not len(message_headder):
            return False

        message_length = int(message_headder.decode("utf-8").strip())
        return{"headder": message_headder,"data": client_socket.recv(message_length)}

        
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            
            clients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
            
        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            user = clients[notified_socket]
            #print(f"Received message from {}")
            print(f"Received message from {user['data'].decode('utf-8')}:{message['data'].decode('utf-8')}")

            # now we need to share this new message with everybody
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['headder'] + user['data'] + message['headder']+message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

        
                    


    
