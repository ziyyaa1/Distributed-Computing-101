import socket

# Step 1: create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect to server
client_socket.connect(("localhost", 8080))

# Step 3: send message
client_socket.send("Hi server!".encode())

# Step 4: receive reply
data = client_socket.recv(1024).decode()
print(f"Server: {data}")

# Step 5: close connection
client_socket.close()
