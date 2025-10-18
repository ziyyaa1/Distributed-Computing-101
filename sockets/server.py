import socket

# Step 1: create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind to an IP + port
server_socket.bind(("localhost", 8080))

# Step 3: listen for connections
server_socket.listen(1)
print("Server listening on port 8080 :)")

# Step 4: accept client connection
client_socket, address = server_socket.accept()
print(f"Connected to {address}")

# Step 5: receive message
data = client_socket.recv(1024).decode()
print(f"Client: {data}")

# Step 6: send reply
client_socket.send("Hello from server!".encode())

# Step 7: close connection
client_socket.close()
server_socket.close()
