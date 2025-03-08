from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread

# Set to store connected clients
clients = set()

# Function to handle client connections
def client_thread(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"{client_address[0]}:{client_address[1]} says: {message}")
            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(f"{client_address[0]}:{client_address[1]} says: {message}".encode("utf-8"))
                    except Exception as e:
                        print(f"Failed to send message to {client_address}: {e}")
        except ConnectionResetError:
            break
        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break

    # Remove the client from the set and close the connection
    clients.remove(client_socket)
    print(f"{client_address[0]}:{client_address[1]} disconnected")
    client_socket.close()

# Create a socket for the server
host_socket = socket(AF_INET, SOCK_STREAM)
host_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Server details
host_ip = "127.0.0.1"
port_number = 7500

# Bind the socket to the host and port
host_socket.bind((host_ip, port_number))
host_socket.listen()
print("Waiting for connections...")

# Accept incoming connections
while True:
    client_socket, client_address = host_socket.accept()
    clients.add(client_socket)
    print(f"Connection established with: {client_address[0]}:{client_address[1]}")
    # Start a new thread for the client
    thread = Thread(target=client_thread, args=(client_socket, client_address))
    thread.start()