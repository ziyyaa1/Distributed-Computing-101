import socket

#1. created a server socket with address type AF and sock stream type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. bind it with address so that anyone can connect to us / find us
server.bind(("localhost", 8080))

#3. Start listening for client connection
server.listen(1) # (1) here means that only 1 client can wait in queue at a time

#4. Print msg to see our web.py is working
print("Listening on http://localhost:8080")

#5.accept client who is waiting to be connected
client, addr = server.accept()

#6. once connected, web.py will print this
print("Connection from:", addr)

#7. read whatever browser has sent upto 1024 bytes and print it
request = client.recv(1024).decode() #decode change it to readale format string 
print("Request:\n", request)

#8. store server's reply to client (imp to have empty line bw header and content)
response = """HTTP/1.1 200 OK
Content-Type: text/html #tells browser that incoming data is in python 

<html><body><h1>Hello from Python!</h1></body></html>
"""

#8. send msg to client browser
client.send(response.encode()) #encode string to byte bcs socket only sends/receive byte

# close client and server communication
client.close()
server.close()
