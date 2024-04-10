import socket

client = socket.socket()

client.connect(("192.168.0.103", 9999))

data = client.recv(1024).decode()
print(data)

client.send("hey, I'm another client..".encode())
client.close()
